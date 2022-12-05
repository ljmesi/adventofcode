#!/usr/bin/env python
"""Find which elf carries the most calories"""
__author__ = "LJM"
__date__ = "2022-12-03"
__version__ = "0.1.0"


import argparse
import dataclasses
import json
import logging
from pathlib import Path
from pydantic.dataclasses import dataclass


@dataclass
class ElfFoods:
    """One Elf and his foods in a list of calories"""

    name: str
    calories: list[int]
    total: int | None = dataclasses.field(
        default=None,
        metadata=dict(title="The total amount of calories the Elf is carrying."),
    )

    def __post_init__(self):
        self.total: int = sum(self.calories)


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""Example usage: ./calories.py -f elfs_and_calories.json""",
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="CALORIES_AND_ELFS_FILE",
        type=Path,
        help="File from which to read which elf carries which foods.",
    )

    return parser.parse_args()


def main() -> None:
    """Main function"""
    # Parse CLI arguments
    args: argparse.Namespace = get_args()
    with open(args.file, encoding="utf8") as fh:
        data = json.load(fh)
        # Unpacking items to keyword arguments (kwargs) with **
        elfs_with_foods: list[ElfFoods] = [ElfFoods(**item) for item in data]
        elfs_with_foods_sorted = sorted(
            elfs_with_foods, key=lambda x: x.total, reverse=True
        )
        elf_with_most_calories = elfs_with_foods_sorted[0]
        print(
            f"{elf_with_most_calories.name} has most calories.\n"
            f"He has {elf_with_most_calories.total} calories."
        )


if __name__ == "__main__":
    main()
