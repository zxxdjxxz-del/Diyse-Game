from __future__ import annotations

import argparse
import csv
from dataclasses import asdict
import json
import sys

from .battle import simulate_advanced
from .core import adjusted_hit_chance, class_multipliers, cumulative_exp, direct_damage, exp_to_next_level, level_from_exp, natural_stats, simulate, sweep_enemy_stats
from .encounters.story_bosses.hollow_watch_castellan import SmartPolicyConfig, simulate_hollow_watch_smart
from .encounters.story_bosses.matron_zevraya import simulate_matron_zevraya
from .io import load_advanced_scenario, load_progression_route, load_scenario
from .overlays import BalanceOverlay
from .progression import (
    ClassCexpState,
    audit_campaign,
    audit_campaign_checkpoint,
    audit_campaign_class_aware_named_checkpoint,
    audit_campaign_named_checkpoint,
    audit_character_checkpoint,
    audit_character_class_aware_named_checkpoint,
    audit_character_named_checkpoint,
    project_progression,
    required_average_exp_per_encounter,
)
from .sources import audit_repo_sources, audit_simulation_readiness


def _csv_floats(value: str) -> list[float]:
    values = [float(item.strip()) for item in value.split(",") if item.strip()]
    if not values:
        raise argparse.ArgumentTypeError("provide at least one numeric value")
    return values


def _csv_names(value: str) -> tuple[str, ...]:
    values = tuple(item.strip() for item in value.split(",") if item.strip())
    if not values:
        raise argparse.ArgumentTypeError("provide at least one name")
    return values


def _class_choice(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("class choice must use CHARACTER=CLASS")
    character, class_name = (part.strip() for part in value.split("=", 1))
    if not character or not class_name:
        raise argparse.ArgumentTypeError("class choice must use non-empty CHARACTER=CLASS")
    return character, class_name


def _class_choice_map(values: list[tuple[str, str]]) -> dict[str, str]:
    choices: dict[str, str] = {}
    for character, class_name in values:
        if character in choices:
            raise SystemExit(f"duplicate --class-choice for {character}")
        choices[character] = class_name
    return choices


def _equipment_choice(value: str) -> tuple[str, str, str]:
    if "=" not in value or ":" not in value.split("=", 1)[0]:
        raise argparse.ArgumentTypeError(
            "equipment choice must use CHARACTER:SLOT=ITEM"
        )
    owner_slot, item = (part.strip() for part in value.split("=", 1))
    character, slot = (part.strip() for part in owner_slot.split(":", 1))
    slot = slot.casefold()
    if not character or not slot or not item:
        raise argparse.ArgumentTypeError(
            "equipment choice must use non-empty CHARACTER:SLOT=ITEM"
        )
    if slot not in {"weapon", "armor", "secondary"}:
        raise argparse.ArgumentTypeError(
            "equipment SLOT must be weapon, armor, or secondary"
        )
    return character, slot, item


def _equipment_choice_map(
    values: list[tuple[str, str, str]],
) -> dict[str, dict[str, str]]:
    choices: dict[str, dict[str, str]] = {}
    for character, slot, item in values:
        character_choices = choices.setdefault(character, {})
        if slot in character_choices:
            raise SystemExit(
                f"duplicate --equipment-choice for {character}:{slot}"
            )
        character_choices[slot] = item
    return choices


def _class_state(value: str) -> tuple[str, ClassCexpState]:
    if ":" not in value:
        raise argparse.ArgumentTypeError(
            "class state must use CHARACTER:base=CEXP,subclass=CEXP"
        )
    character, raw_fields = (part.strip() for part in value.split(":", 1))
    if not character or not raw_fields:
        raise argparse.ArgumentTypeError(
            "class state must use non-empty CHARACTER:base=CEXP,subclass=CEXP"
        )

    fields: dict[str, int] = {}
    for raw_field in raw_fields.split(","):
        if "=" not in raw_field:
            raise argparse.ArgumentTypeError(
                "class state fields must use base=CEXP and subclass=CEXP"
            )
        raw_key, raw_cexp = (part.strip() for part in raw_field.split("=", 1))
        key = raw_key.casefold()
        if key not in {"base", "subclass"}:
            raise argparse.ArgumentTypeError(
                "class state fields must be base and subclass"
            )
        if key in fields:
            raise argparse.ArgumentTypeError(f"duplicate class state field: {key}")
        try:
            fields[key] = int(raw_cexp.replace(",", ""))
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"class state {key} CEXP must be an integer"
            ) from exc

    missing = {"base", "subclass"} - set(fields)
    if missing:
        raise argparse.ArgumentTypeError(
            "class state requires both base=CEXP and subclass=CEXP"
        )
    try:
        state = ClassCexpState(
            base_cexp=fields["base"],
            subclass_cexp=fields["subclass"],
        )
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    return character, state


def _class_state_map(
    values: list[tuple[str, ClassCexpState]],
) -> dict[str, ClassCexpState]:
    states: dict[str, ClassCexpState] = {}
    for character, state in values:
        if character in states:
            raise SystemExit(f"duplicate --class-state for {character}")
        states[character] = state
    return states


def _markdown_cell(value: object) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def _print_audit_rows(rows, output_format: str) -> None:
    payload = [row.as_dict() for row in rows]
    if output_format == "json":
        print(json.dumps(payload, indent=2))
        return
    if not payload:
        return

    fieldnames = list(payload[0])
    if output_format == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(payload)
        return

    print("| " + " | ".join(fieldnames) + " |")
    print("| " + " | ".join("---" for _ in fieldnames) + " |")
    for row in payload:
        print("| " + " | ".join(_markdown_cell(row[field]) for field in fieldnames) + " |")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="diysim", description="Diyse balance calculation and battle simulator")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("audit-sources", help="verify simulator source authority can be resolved from the repo")

    readiness = sub.add_parser("audit-readiness", help="scan enemy/boss/Hunt owner files for simulation blockers")
    readiness.add_argument("--summary-only", action="store_true", help="omit per-file detail")
    readiness.add_argument("--issues-only", action="store_true", help="print only the filtered blocker list")
    readiness.add_argument("--severity", choices=("all", "source_gap", "parser_gap"), default="all")
    readiness.add_argument("--strict", action="store_true", help="return exit code 2 when any source/parser gap is found")

    progression_audit = sub.add_parser(
        "progression-audit",
        help="resolve source-backed character loadouts and calculated stats by chapter/checkpoint",
    )
    progression_audit.add_argument(
        "--route",
        choices=("mandatory", "expected", "best_available"),
        default="mandatory",
        help="progression/loadout assumption; unresolved authority is reported as a source gap",
    )
    progression_audit.add_argument("--chapter", type=int, help="audit one end-of-chapter target")
    progression_audit.add_argument(
        "--checkpoint",
        help="audit one named campaign checkpoint, e.g. end_ch7, ch13_start, ch13_last_shelter, ch13_ending",
    )
    progression_audit.add_argument("--start-chapter", type=int, default=0, help="first chapter when auditing a range")
    progression_audit.add_argument("--end-chapter", type=int, default=13, help="last chapter when auditing a range")
    progression_audit.add_argument("--character", help="filter to one permanent character")
    progression_audit.add_argument(
        "--class-choice",
        action="append",
        type=_class_choice,
        default=[],
        metavar="CHARACTER=CLASS",
        help="explicit selected class for a simulation route; repeat for multiple characters",
    )
    progression_audit.add_argument(
        "--class-state",
        action="append",
        type=_class_state,
        default=[],
        metavar="CHARACTER:base=CEXP,subclass=CEXP",
        help=(
            "validated mandatory-route Base/Subclass CEXP state at an exact named checkpoint; "
            "repeat for multiple characters"
        ),
    )
    progression_audit.add_argument(
        "--equipment-choice",
        action="append",
        type=_equipment_choice,
        default=[],
        metavar="CHARACTER:SLOT=ITEM",
        help=(
            "explicit assumed-owned Ordinary equipment for a simulation snapshot; repeat per slot. "
            "Native gear uses ordinary access; reciprocal donor gear additionally requires a "
            "validated --class-state and the source-backed Subclass Class Level gate"
        ),
    )
    progression_audit.add_argument("--format", choices=("json", "csv", "markdown"), default="markdown")
    progression_audit.add_argument(
        "--strict",
        action="store_true",
        help="return exit code 2 when any returned row has unresolved source authority",
    )

    stats = sub.add_parser("stats", help="calculate natural stats from current repo authority")
    stats.add_argument("level", type=int)
    stats.add_argument("--class", dest="class_name", choices=sorted(class_multipliers()))
    for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed"):
        stats.add_argument(f"--equip-{key}", type=int, default=0)

    exp = sub.add_parser("exp", help="inspect current repo Player-EXP progression")
    group = exp.add_mutually_exclusive_group(required=True)
    group.add_argument("--level", type=int)
    group.add_argument("--current-exp", type=int)

    hit = sub.add_parser("hit", help="calculate final Base Hit chance")
    hit.add_argument("base_hit", type=int)
    hit.add_argument("evasion", type=int)

    damage = sub.add_parser("damage", help="calculate one direct hit")
    damage.add_argument("kind", choices=("physical", "magical", "hybrid"))
    damage.add_argument("--attack", type=float, default=0)
    damage.add_argument("--magic", type=float, default=0)
    damage.add_argument("--defense", type=float, default=0)
    damage.add_argument("--spirit", type=float, default=0)
    damage.add_argument("--power", type=float, required=True)
    damage.add_argument("--def-pen", type=float, default=0)
    damage.add_argument("--spr-pen", type=float, default=0)
    damage.add_argument("--physical-weight", type=float)
    damage.add_argument("--magical-weight", type=float)
    damage.add_argument("--crit", action="store_true")
    damage.add_argument("--reduction", type=float, default=0)

    sim = sub.add_parser("simulate", help="run simple Monte Carlo direct-battle tests")
    sim.add_argument("scenario")
    sim.add_argument("--runs", type=int, default=10_000)
    sim.add_argument("--seed", type=int, default=1)

    advanced = sub.add_parser("simulate-advanced", help="run MP/element/status/healing battle tests")
    advanced.add_argument("scenario")
    advanced.add_argument("--runs", type=int, default=10_000)
    advanced.add_argument("--seed", type=int, default=1)

    hollow_watch = sub.add_parser("hollow-watch", help="run Hollow Watch from current repo authority")
    hollow_watch.add_argument("--runs", type=int, default=20_000)
    hollow_watch.add_argument("--seed", type=int, default=93)
    hollow_watch.add_argument("--heal-trigger", type=float, default=0.55, help="simulator policy threshold; not Diyse canon")

    zevraya = sub.add_parser("zevraya", help="run Matron Zevraya from repo authority plus explicit working overlays")
    zevraya.add_argument("--player-level", type=int, default=24)
    zevraya.add_argument("--structure", choices=("owner", "non_diluting"), default="owner")
    zevraya.add_argument("--strategy", choices=("rush", "dismantle"), default="rush")
    zevraya.add_argument(
        "--reservoir-plan",
        type=_csv_names,
        help="ordered selective dismantle plan, e.g. Brood,Conduction; valid only with --strategy dismantle",
    )
    zevraya.add_argument("--power-multiplier", type=float, default=1.0)
    zevraya.add_argument("--boss-level-offset", type=int, default=0)
    zevraya.add_argument("--runs", type=int, default=1_000)
    zevraya.add_argument("--seed", type=int, default=104)
    zevraya.add_argument("--no-prepared", action="store_true", help="disable the working finite prepared-inventory benchmark")

    sweep = sub.add_parser("sweep", help="sweep enemy HP/ATK/DEF multipliers")
    sweep.add_argument("scenario")
    sweep.add_argument("--hp", type=_csv_floats, default=[1.0])
    sweep.add_argument("--attack", type=_csv_floats, default=[1.0])
    sweep.add_argument("--defense", type=_csv_floats, default=[1.0])
    sweep.add_argument("--runs", type=int, default=2_000)
    sweep.add_argument("--seed", type=int, default=1)

    route = sub.add_parser("route", help="project a Player-EXP route from JSON")
    route.add_argument("route_file")

    solve = sub.add_parser("solve-exp", help="solve required average encounter EXP for a target level checkpoint")
    solve.add_argument("--start-exp", type=int)
    solve.add_argument("--start-level", type=int)
    solve.add_argument("--target-level", type=int, required=True)
    solve.add_argument("--target-progress", type=float, default=0.0)
    solve.add_argument("--encounters", type=int, required=True)
    solve.add_argument("--fixed-exp", type=int, default=0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "audit-sources":
        report = audit_repo_sources()
        print(json.dumps(report.as_dict(), indent=2))
        return 0 if report.ok else 2
    if args.command == "audit-readiness":
        report = audit_simulation_readiness()
        payload = report.issues_dict(args.severity) if args.issues_only else report.as_dict(include_files=not args.summary_only)
        print(json.dumps(payload, indent=2))
        if args.strict and (report.source_gaps or report.parser_gaps):
            return 2
        return 0
    if args.command == "progression-audit":
        class_choices = _class_choice_map(args.class_choice)
        class_states = _class_state_map(args.class_state)
        equipment_choices = _equipment_choice_map(args.equipment_choice)
        if args.character:
            unrelated = sorted(
                (set(class_choices) | set(class_states) | set(equipment_choices)) - {args.character}
            )
            if unrelated:
                raise SystemExit(
                    "--character cannot be combined with class/class-state/equipment choices for "
                    "other characters: " + ", ".join(unrelated)
                )

        if args.chapter is not None and args.checkpoint is not None:
            raise SystemExit("--chapter and --checkpoint are mutually exclusive")
        if (args.chapter is not None or args.checkpoint is not None) and (
            args.start_chapter != 0 or args.end_chapter != 13
        ):
            raise SystemExit(
                "--chapter/--checkpoint cannot be combined with --start-chapter/--end-chapter"
            )
        if class_states and args.checkpoint is None:
            raise SystemExit(
                "--class-state requires --checkpoint because Class CEXP validation uses exact "
                "named campaign checkpoints"
            )
        if class_states and args.route != "mandatory":
            raise SystemExit(
                "--class-state currently supports --route mandatory only; optional/route-specific "
                "CEXP is not yet modeled"
            )

        try:
            if args.checkpoint is not None:
                if class_states:
                    if args.character:
                        rows = (
                            audit_character_class_aware_named_checkpoint(
                                args.character,
                                args.checkpoint,
                                args.route,
                                selected_class=class_choices.get(args.character),
                                equipment_choices=equipment_choices.get(args.character),
                                class_state=class_states.get(args.character),
                            ),
                        )
                    else:
                        rows = audit_campaign_class_aware_named_checkpoint(
                            args.checkpoint,
                            args.route,
                            class_choices=class_choices,
                            equipment_choices=equipment_choices,
                            class_states=class_states,
                        )
                elif args.character:
                    rows = (
                        audit_character_named_checkpoint(
                            args.character,
                            args.checkpoint,
                            args.route,
                            selected_class=class_choices.get(args.character),
                            equipment_choices=equipment_choices.get(args.character),
                        ),
                    )
                else:
                    rows = audit_campaign_named_checkpoint(
                        args.checkpoint,
                        args.route,
                        class_choices=class_choices,
                        equipment_choices=equipment_choices,
                    )
            elif args.chapter is not None:
                if not 0 <= args.chapter <= 13:
                    raise SystemExit("--chapter must be between 0 and 13")
                if args.character:
                    rows = (
                        audit_character_checkpoint(
                            args.character,
                            args.chapter,
                            args.route,
                            selected_class=class_choices.get(args.character),
                            equipment_choices=equipment_choices.get(args.character),
                        ),
                    )
                else:
                    rows = audit_campaign_checkpoint(
                        args.chapter,
                        args.route,
                        class_choices=class_choices,
                        equipment_choices=equipment_choices,
                    )
            else:
                if not 0 <= args.start_chapter <= args.end_chapter <= 13:
                    raise SystemExit("chapter range must satisfy 0 <= start <= end <= 13")
                rows = audit_campaign(
                    args.route,
                    start_chapter=args.start_chapter,
                    end_chapter=args.end_chapter,
                    class_choices=class_choices,
                    equipment_choices=equipment_choices,
                )
                if args.character:
                    rows = tuple(row for row in rows if row.character == args.character)
                    if not rows:
                        raise SystemExit(
                            f"no recruited audit rows found for {args.character!r} in the selected chapter range"
                        )
        except (KeyError, ValueError, TypeError) as exc:
            raise SystemExit(str(exc)) from exc

        _print_audit_rows(rows, args.format)
        if args.strict and any(not row.authority_complete for row in rows):
            return 2
        return 0
    if args.command == "stats":
        equipment = {key: getattr(args, f"equip_{key}") for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")}
        print(json.dumps(natural_stats(args.level, args.class_name, equipment).as_dict(), indent=2))
    elif args.command == "exp":
        if args.level is not None:
            print(json.dumps({"level": args.level, "cumulative_exp": cumulative_exp(args.level)}, indent=2))
        else:
            print(json.dumps({"current_exp": args.current_exp, "level": level_from_exp(args.current_exp), "exp_to_next": exp_to_next_level(args.current_exp)}, indent=2))
    elif args.command == "hit":
        print(adjusted_hit_chance(args.base_hit, args.evasion))
    elif args.command == "damage":
        if args.kind == "hybrid" and (args.physical_weight is None or args.magical_weight is None):
            raise SystemExit("hybrid damage requires --physical-weight and --magical-weight")
        print(direct_damage(
            args.kind,
            attack=args.attack, magic=args.magic, defense=args.defense, spirit=args.spirit,
            power=args.power, defense_penetration=args.def_pen, spirit_penetration=args.spr_pen,
            physical_weight=args.physical_weight, magical_weight=args.magical_weight,
            crit=args.crit, direct_damage_reduction=args.reduction,
        ))
    elif args.command == "simulate":
        print(json.dumps(simulate(load_scenario(args.scenario), runs=args.runs, seed=args.seed).as_dict(), indent=2))
    elif args.command == "simulate-advanced":
        print(json.dumps(simulate_advanced(load_advanced_scenario(args.scenario), runs=args.runs, seed=args.seed).as_dict(), indent=2))
    elif args.command == "hollow-watch":
        summary = simulate_hollow_watch_smart(
            policy=SmartPolicyConfig(heal_trigger_hp_fraction=args.heal_trigger),
            runs=args.runs,
            seed=args.seed,
        )
        print(json.dumps(asdict(summary), indent=2))
    elif args.command == "zevraya":
        summary = simulate_matron_zevraya(
            player_level=args.player_level,
            structure_mode=args.structure,
            strategy=args.strategy,
            reservoir_plan=args.reservoir_plan,
            overlay=BalanceOverlay(
                direct_damage_power_multiplier=args.power_multiplier,
                effective_stat_level_offset=args.boss_level_offset,
            ),
            use_prepared_inventory=not args.no_prepared,
            runs=args.runs,
            seed=args.seed,
        )
        print(json.dumps(asdict(summary), indent=2))
    elif args.command == "sweep":
        rows = sweep_enemy_stats(load_scenario(args.scenario), hp_multipliers=args.hp, attack_multipliers=args.attack, defense_multipliers=args.defense, runs=args.runs, seed=args.seed)
        print(json.dumps(rows, indent=2))
    elif args.command == "route":
        start_exp, segments = load_progression_route(args.route_file)
        print(json.dumps(project_progression(start_exp, segments).as_dict(), indent=2))
    elif args.command == "solve-exp":
        if args.start_exp is not None and args.start_level is not None:
            raise SystemExit("use either --start-exp or --start-level, not both")
        if args.start_exp is None and args.start_level is None:
            raise SystemExit("provide --start-exp or --start-level")
        start_exp = args.start_exp if args.start_exp is not None else cumulative_exp(args.start_level)
        average = required_average_exp_per_encounter(start_exp=start_exp, target_level=args.target_level, target_level_progress=args.target_progress, encounter_count=args.encounters, fixed_exp=args.fixed_exp)
        print(json.dumps({"start_exp": start_exp, "target_level": args.target_level, "target_progress": args.target_progress, "encounters": args.encounters, "fixed_exp": args.fixed_exp, "required_average_exp_per_encounter": average}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())