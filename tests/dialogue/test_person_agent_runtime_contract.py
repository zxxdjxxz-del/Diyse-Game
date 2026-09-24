#!/usr/bin/env python3
from __future__ import annotations

import ast
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PERSON_AGENT_PATH = ROOT / "external-services/canary/person_agent.py"
ORCHESTRATOR_PATH = ROOT / "external-services/canary/scene_orchestrator.py"
COMPILER_PATH = ROOT / "tools/dialogue/compile_scene_authority.py"
DIALOGUE_SYSTEM_PATH = ROOT / "external-services/canary/context/dialogue_system.yaml"
BRAIN_DIR = ROOT / "external-services/canary/brains"

PERMANENT_SIX = ("cyanis", "ilyra", "torren", "nimera", "vaelira", "seyrik")
NON_RUNTIME_BRAIN_KEYS = {"schema_version", "status"}


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compact_brain_allowlist(source: str) -> set[str]:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or node.name != "compact_brain":
            continue
        for statement in node.body:
            if not isinstance(statement, ast.Assign):
                continue
            if not any(isinstance(target, ast.Name) and target.id == "keys" for target in statement.targets):
                continue
            if not isinstance(statement.value, (ast.List, ast.Tuple)):
                continue
            values: set[str] = set()
            for item in statement.value.elts:
                if isinstance(item, ast.Constant) and isinstance(item.value, str):
                    values.add(item.value)
            return values
    raise AssertionError("Could not locate compact_brain() key allowlist")


def main() -> int:
    person_source = PERSON_AGENT_PATH.read_text(encoding="utf-8")
    orchestrator_source = ORCHESTRATOR_PATH.read_text(encoding="utf-8")
    compiler_source = COMPILER_PATH.read_text(encoding="utf-8")

    # Syntax-only regression checks do not require configured services or a model.
    ast.parse(person_source)
    ast.parse(orchestrator_source)
    ast.parse(compiler_source)

    runtime_keys = compact_brain_allowlist(person_source)

    for character_id in PERMANENT_SIX:
        brain_path = BRAIN_DIR / f"{character_id}.yaml"
        brain = yaml.safe_load(brain_path.read_text(encoding="utf-8"))
        expect(isinstance(brain, dict), f"{character_id} brain must parse as a mapping")

        expected_runtime_keys = set(brain.keys()) - NON_RUNTIME_BRAIN_KEYS
        missing = sorted(expected_runtime_keys - runtime_keys)
        expect(
            not missing,
            f"{character_id} has top-level brain sections omitted by compact_brain(): {missing}",
        )

    shared = yaml.safe_load(DIALOGUE_SYSTEM_PATH.read_text(encoding="utf-8"))
    expect(isinstance(shared, dict), "dialogue_system.yaml must parse as a mapping")
    expect(int(shared.get("schema_version", 0)) >= 2, "dialogue runtime schema must be v2+")

    reliability = shared.get("runtime_reliability_contract", {})
    expect(isinstance(reliability, dict), "runtime_reliability_contract missing")
    expect(
        reliability.get("principle") == "hard_canon_cannot_drift_human_recall_can",
        "hard-canon / human-recall reliability principle missing",
    )

    retrieval = reliability.get("memory_retrieval", {})
    expect(
        retrieval.get("hard_rule") == "relevance_never_bypasses_authorization",
        "authorize-before-relevance memory rule missing",
    )

    relationship = reliability.get("relationship_runtime_vector", {})
    expect(
        relationship.get("principle") == "no_single_friendship_number",
        "multidimensional relationship-state rule missing",
    )

    dynamics = reliability.get("conversation_dynamics", {})
    expect(isinstance(dynamics, dict), "conversation_dynamics contract missing")
    expect("floor_model" in dynamics, "conversation floor model missing")
    expect("topic_model" in dynamics, "conversation topic model missing")
    expect("open_threads" in dynamics, "open-thread model missing")

    expect(
        "person_runtime_context: dict[str, Any]" in person_source,
        "Person Agent turn request is missing person_runtime_context",
    )
    expect(
        "authorized_memories_for_turn" in person_source,
        "Person Agent memory authorization filter is missing",
    )
    expect(
        "person_runtime_contexts: dict[str, dict[str, Any]]" in orchestrator_source,
        "Scene Orchestrator is missing per-person runtime contexts",
    )
    expect(
        'context.setdefault("memory_authorization", {"mode": "none"})' in orchestrator_source,
        "Scene Orchestrator must deny persistent memory by default",
    )
    expect(
        '"person_runtime_contexts": person_runtime_contexts' in compiler_source,
        "Authority compiler must emit per-person runtime contexts",
    )

    print("Diyse Person Agent runtime-contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
