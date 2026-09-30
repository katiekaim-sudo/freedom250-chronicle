#!/usr/bin/env python3
"""Build the Fine Print chart projection from its derived seed."""
from pathlib import Path

from timeline_machine_astro import build_file

HERE = Path(__file__).absolute().parent
SEED = HERE / "fine_print_seed.json"
OUT = HERE / "fine_print_astro.json"
AMERICA_PRE_GRID = {}
COMMENT = ("Charts for the Fine Print timeline. Noon D.C. for releases, midnight for scheduled "
           "dates (Katie 2026-07-11). Whole Sign. 916 America absent pre-2024 (grid bound).")
GENERATED = "2026-07-12"


def main():
    chart_count, without_america = build_file(
        SEED, OUT, COMMENT, GENERATED, AMERICA_PRE_GRID)
    print(f"cast {chart_count} charts ({without_america} without America, pre-grid) -> {OUT}")


if __name__ == "__main__":
    main()
