import pathlib


def load_data():
    return [
        tuple(round.split())
        for round in pathlib.Path("inputs/day_02/data.txt").read_text().split("\n")
    ]


WIN_POINTS = {
    ("A", "Y"): 6,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("A", "X"): 3,
    ("B", "Y"): 3,
    ("C", "Z"): 3,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("C", "Y"): 0,
}
CHOICE_POINT = dict(zip("XYZ", [1, 2, 3]))


def part_one():
    elf_data = load_data()
    print(sum(WIN_POINTS[round] + CHOICE_POINT[round[1]] for round in elf_data))


CHOICE = {
    # rock
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",
    # paper
    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",
    # scissors
    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X",
}
WIN_POINTS_TW0 = dict(zip("XYZ", [0, 3, 6]))


def part_two():
    elf_data = load_data()
    print(
        sum(
            WIN_POINTS_TW0[round[1]] + CHOICE_POINT[CHOICE[round]] for round in elf_data
        )
    )


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
