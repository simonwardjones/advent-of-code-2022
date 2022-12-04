from itertools import zip_longest
import pathlib
from string import ascii_lowercase
from string import ascii_uppercase

POINTS = {
    **dict(zip(ascii_lowercase, range(1, 27))),
    **dict(zip(ascii_uppercase, range(27, 53))),
}


def load_data():
    return pathlib.Path("inputs/day_03/data.txt").read_text().split()


def part_one():
    duplicates = []
    for backpack in load_data():
        items = int(len(backpack) / 2)
        compartments = (set(backpack[:items]), set(backpack[items:]))
        duplicate = list(compartments[0] & compartments[1])[0]
        duplicates.append(duplicate)
    print(sum(POINTS[item] for item in duplicates))


def part_two():
    elf_data = load_data()
    total = 0
    for bag1, bag2, bag3 in zip_longest(*[iter(elf_data)] * 3):
        total += POINTS[list(set(bag1) & set(bag2) & set(bag3))[0]]
    print(total)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
