import pathlib
import re


def load_data():
    return pathlib.Path("inputs/day_06/data.txt").read_text()


def part_one():
    elf_data = load_data()
    for letter_id, letter in enumerate(elf_data):
        test = elf_data[letter_id : letter_id + 4]
        if len(test) == len(set(test)):
            print(letter_id + 4)
            break


def part_two():
    elf_data = load_data()
    print(elf_data)
    for letter_id, letter in enumerate(elf_data):
        test = elf_data[letter_id : letter_id + 14]
        if len(test) == len(set(test)):
            print(letter_id + 14)
            break


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
