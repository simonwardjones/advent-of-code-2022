from itertools import zip_longest
from operator import itemgetter
import pathlib
from functools import cmp_to_key
from typing import Iterable


def load_data():
    return pathlib.Path("inputs/day_13/data.txt").read_text()


def part_one():
    elf_data = [list(map(eval, group.split())) for group in load_data().split("\n\n")]
    results = [compare(left, right) for left, right in elf_data]
    print(sum(map(itemgetter(0), filter(lambda x: x[1] > 0, enumerate(results, 1)))))


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if isinstance(left, int) and isinstance(right, Iterable):
        if not right:
            return -1  # right ran out first.
        comp = compare(left, right[0])
        if comp == 0 and len(right) > 1:
            return 1  # left ran out first
        return comp

    if isinstance(left, Iterable) and isinstance(right, int):
        if not left:
            return 1  # left ran out first.
        comp = compare(left[0], right)
        if comp == 0 and len(left) > 1:
            return -1
        return comp

    for new_left, new_right in zip_longest(left, right):
        if new_left is None:
            return 1
        if new_right is None:
            return -1
        comp = compare(new_left, new_right)
        if comp != 0:
            return comp

    return 0


def part_two():
    data = (
        load_data()
        .replace("\n\n", "\n")
        .replace("[", "(")
        .replace("]", ")")
        .split("\n")
    )
    elf_data = tuple(eval(group) for group in data) + (((2)), ((6)))
    sorted_items = sorted(elf_data, key=cmp_to_key(compare), reverse=True)
    print((sorted_items.index(((2))) + 1) * (sorted_items.index(((6))) + 1))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
