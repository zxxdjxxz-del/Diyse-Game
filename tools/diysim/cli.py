from __future__ import annotations

import argparse
import json

from .core import (
    CLASS_MULTIPLIERS,
    adjusted_hit_chance,
    cumulative_exp,
    direct_damage,
    exp_to_next_level,
    level_from_exp,
    natural_stats,
    simulate,
    sweep_enemy_stats,
)
from .io import load_scenario


def _csv_floats(value: str) -> list[float]:
    values = [float(item.strip()) for item in value.split(",") if item.strip()]
    if not values:
        raise argparse.ArgumentTypeError("provide at least one numeric value")
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="diysim", description="Diyse balance calculation and direct-battle simulator")
    sub = parser.add_subparsers(dest="command", required=True)

    stats = sub.add_parser("stats", help="calculate natural stats")
    stats.add_argument("level", type=int)
    stats.add_argument("--class", dest="class_name", choices=sorted(CLASS_MULTIPLIERS))
    for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed"):
        stats.add_argument(f"--equip-{key}", type=int, default=0)

    exp = sub.add_parser("exp", help="inspect level/EXP progression")
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
    damage.add_argument("--physical-weight", type=float, default=0.5)
    damage.add_argument("--magical-weight", type=float, default=0.5)
    damage.add_argument("--crit", action="store_true")
    damage.add_argument("--reduction", type=float, default=0)

    sim = sub.add_parser("simulate", help="run Monte Carlo direct-battle tests")
    sim.add_argument("scenario")
    sim.add_argument("--runs", type=int, default=10_000)
    sim.add_argument("--seed", type=int, default=1)

    sweep = sub.add_parser("sweep", help="sweep enemy HP/ATK/DEF multipliers")
    sweep.add_argument("scenario")
    sweep.add_argument("--hp", type=_csv_floats, default=[1.0])
    sweep.add_argument("--attack", type=_csv_floats, default=[1.0])
    sweep.add_argument("--defense", type=_csv_floats, default=[1.0])
    sweep.add_argument("--runs", type=int, default=2_000)
    sweep.add_argument("--seed", type=int, default=1)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
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
        print(direct_damage(
            args.kind,
            attack=args.attack,
            magic=args.magic,
            defense=args.defense,
            spirit=args.spirit,
            power=args.power,
            defense_penetration=args.def_pen,
            spirit_penetration=args.spr_pen,
            physical_weight=args.physical_weight,
            magical_weight=args.magical_weight,
            crit=args.crit,
            direct_damage_reduction=args.reduction,
        ))
    elif args.command == "simulate":
        summary = simulate(load_scenario(args.scenario), runs=args.runs, seed=args.seed)
        print(json.dumps(summary.as_dict(), indent=2))
    elif args.command == "sweep":
        rows = sweep_enemy_stats(
            load_scenario(args.scenario),
            hp_multipliers=args.hp,
            attack_multipliers=args.attack,
            defense_multipliers=args.defense,
            runs=args.runs,
            seed=args.seed,
        )
        print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
