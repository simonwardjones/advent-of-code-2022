import pathlib


def load_data():
    return [
        sum(int(calorie) for calorie in elf_calories.split())
        for elf_calories in pathlib.Path("inputs/day_01/data.txt")
        .read_text()
        .split("\n\n")
    ]


def part_one():
    elf_data = load_data()
    print(max(elf_data))


def part_two():
    elf_data = load_data()
    print(sum(sorted(elf_data)[-3:]))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
