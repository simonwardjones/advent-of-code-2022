import pathlib
import re


def load_data():
    return pathlib.Path("inputs/day_04/data.txt").read_text().split()


def part_one():
    elf_data = load_data()
    data = [list(map(int, re.findall(r"\d+", pair))) for pair in elf_data]
    ranges = [(ranges[:2], ranges[2:]) for ranges in data]
    total = 0
    for elf1, elf2 in ranges:
        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (
            elf2[0] <= elf1[0] and elf2[1] >= elf1[1]
        ):
            total += 1
    print(total)


def part_two():
    elf_data = load_data()
    data = [list(map(int, re.findall(r"\d+", pair))) for pair in elf_data]
    ranges = [(ranges[:2], ranges[2:]) for ranges in data]
    total = 0
    for elf1, elf2 in ranges:
        if (elf1[1] >= elf2[0] and elf1[0] <= elf2[1]) or (
            elf2[1] >= elf1[0] and elf2[0] <= elf1[1]
        ):
            total += 1
    print(total)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
