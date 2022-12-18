from operator import itemgetter
import pathlib
import re


def load_data():
    return pathlib.Path("inputs/day_15/data.txt").read_text().split("\n")


def part_one():
    elf_data = [list(map(int, re.findall(r"-?\d+", row))) for row in load_data()]
    no_beacon = {}
    y = 2000000
    y = 10
    distances = []
    for sx, sy, bx, by in elf_data:
        distance = abs(sx - bx) + abs(sy - by)
        distances.append(distance)
        if abs(sy - y) <= distance:  # we touch
            for i in range(distance - abs(sy - y) + 1):
                no_beacon[sx + i] = True
                no_beacon[sx - i] = True
        if by == y:
            no_beacon[bx] = False
    # print(no_beacon)
    # print(no_beacon)
    print(len(list(filter(itemgetter(1), no_beacon.items()))))


def part_two():
    elf_data = [list(map(int, re.findall(r"-?\d+", row))) for row in load_data()]
    bound = 20
    bound = 4000000
    for y in range(bound + 1):
        if y % 10000 == 0:
            print(f"checking {y}")
        ranges = []
        for sx, sy, bx, by in elf_data:
            distance = abs(sx - bx) + abs(sy - by)
            if abs(sy - y) <= distance:  # we touch
                ranges.append(
                    (sx - (distance - abs(sy - y)), sx + (distance - abs(sy - y)))
                )
        ranges = sorted(ranges)
        merge_range = list(ranges[0])
        for mini_range in ranges[1:]:
            if merge_range[1] >= bound:
                break
            if mini_range[0] <= merge_range[1] + 1:
                merge_range[1] = max(merge_range[1], mini_range[1])
            else:
                print("WARNINING", merge_range[1] + 1, y)
                exit
        # print(len(list(filter(itemgetter(1), no_beacon.items()))))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
