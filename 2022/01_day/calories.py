#!/usr/bin/env python
"""Find which elf carries the most calories"""
__author__ = "LJM"
__date__ = "2022-12-03"
__version__ = "0.1.0"


import argparse
import dataclasses
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


def main():
    """Main function"""
    # Parse CLI arguments
    args: argparse.Namespace = get_args()

    counter: int = 1
    current_elf_calories: list = []
    all_elf_calories: list = []

    with open(args.file, encoding="utf8") as filehandle:
        for element in [line.rstrip() for line in filehandle]:
            if element:
                current_elf_calories.append(int(element))
            else:
                all_elf_calories.append(
                    {"name": f"Elf{counter}", "calories": current_elf_calories.copy()}
                )
                current_elf_calories.clear()
                counter += 1

    # Sort the elfs by calories
    elfs_with_foods: list[ElfFoods] = [ElfFoods(**elf) for elf in all_elf_calories]
    elfs_with_foods_sorted = sorted(
        elfs_with_foods, key=lambda x: x.total, reverse=True
    )
    # Pick the one with the most
    elf_with_most_calories: ElfFoods = elfs_with_foods_sorted[0]
    print(
        f"{elf_with_most_calories.name} has most calories.\n"
        f"He has {elf_with_most_calories.total} calories."
    )


if __name__ == "__main__":
    main()
