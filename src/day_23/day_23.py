from collections import defaultdict
import pathlib
from operator import attrgetter


def load_data():
    return {
        complex(row_id, col_id)
        for row_id, row in enumerate(
            pathlib.Path("inputs/day_23/data.txt").read_text().split("\n")
        )
        for col_id, item in enumerate(row)
        if item == "#"
    }


DIRECTIONS = {
    "N": -1,
    "NE": -1 + 1j,
    "E": 1j,
    "SE": 1 + 1j,
    "S": 1,
    "NW": -1 - 1j,
    "W": -1j,
    "SW": 1 - 1j,
}

ORDERED_DIRECTIONS = [
    (-1 - 1j, -1, -1 + 1j),
    (1 + 1j, 1, 1 - 1j),
    (-1 - 1j, -1j, 1 - 1j),
    (-1 + 1j, 1j, 1 + 1j),
]


def display_map(data):
    print(
        "\n".join(
            "".join("#" if complex(row, col) in data else "." for col in range(13))
            for row in range(12)
        )
    )


def part_one():
    elf_data = load_data()
    n_rounds = 10
    check_first = 0
    for _ in range(n_rounds):
        proposed = defaultdict(list)  # proposal:fallback
        for elf in elf_data:
            if all(
                elf + direction not in elf_data for direction in DIRECTIONS.values()
            ):
                proposed[elf].append(elf)
                continue
            for i in range(4):
                check_directions = ORDERED_DIRECTIONS[(check_first + i) % 4]
                if all(
                    elf + direction not in elf_data for direction in check_directions
                ):
                    next_point = elf + check_directions[1]
                    proposed[next_point].append(elf)
                    break
            else:
                proposed[elf].append(elf)
        next_round = set()
        for next_point, elves in proposed.items():
            if len(elves) == 1:
                next_round.add(next_point)
            else:
                next_round = next_round.union(elves)
        check_first = (check_first + 1) % 4
        elf_data = next_round
        Mr, mr = int(max(x.real for x in elf_data)), int(min(x.real for x in elf_data))
        Mc, mc = int(max(x.imag for x in elf_data)), int(min(x.imag for x in elf_data))
        rows = Mr - mr + 1
        cols = Mc - mc + 1
    print(rows * cols - len(elf_data))


def part_two():
    elf_data = load_data()
    check_first = 0
    N = len(elf_data)
    m = 0
    rounds = 0
    while m != N:
        rounds += 1
        m = 0
        proposed = defaultdict(list)  # proposal:fallback
        for elf in elf_data:
            if all(
                elf + direction not in elf_data for direction in DIRECTIONS.values()
            ):
                proposed[elf].append(elf)
                m += 1
                continue
            for i in range(4):
                check_directions = ORDERED_DIRECTIONS[(check_first + i) % 4]
                if all(
                    elf + direction not in elf_data for direction in check_directions
                ):
                    next_point = elf + check_directions[1]
                    proposed[next_point].append(elf)
                    break
            else:
                proposed[elf].append(elf)
        next_round = set()
        for next_point, elves in proposed.items():
            if len(elves) == 1:
                next_round.add(next_point)
            else:
                next_round = next_round.union(elves)
        check_first = (check_first + 1) % 4
        elf_data = next_round
    print(rounds)


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
