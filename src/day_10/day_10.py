from operator import mul
from itertools import starmap, islice, count
import pathlib


def load_data():
    return pathlib.Path("inputs/day_10/data.txt").read_text()


def part_one():
    elf_data = [row.split(" ") for row in load_data().split("\n")]
    register = [0, 1]
    for instruction in elf_data:
        register.append(register[-1])
        if instruction[0] == "addx":
            register.append(register[-1] + int(instruction[1]))
    print(sum(starmap(mul, islice(enumerate(register), 20, None, 40))))


def part_two():
    elf_data = [row.split(" ") for row in load_data().split("\n")]

    sprites = [1]
    for instruction in elf_data:
        sprites.append(sprites[-1])
        if instruction[0] == "addx":
            sprites.append(sprites[-1] + int(instruction[1]))
    out = [[" "] * 40 for _ in range(6)]
    for i, s in enumerate(sprites[:-1]):
        row, col = i // 40, i % 40
        out[row][col] = "#" if abs(col - s) < 2 else "."
    print("\n".join("".join(row) for row in out))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
