from functools import reduce
from operator import mul, add
from collections import deque
import pathlib
import re


def load_data():
    return pathlib.Path("inputs/day_11/data.txt").read_text()


def get_monkeys():
    elf_data = load_data()
    monkeys = []
    for group in elf_data.split("\n\n"):
        monkey = []
        data = group.split("\n")
        monkey.append(deque(int(worry) for worry in re.findall(r"\d+", data[1])))
        monkey.append(data[2].split("=")[-1])
        monkey.append(int(data[3].split(" ")[-1]))
        monkey.append(int(data[4].split(" ")[-1]))
        monkey.append(int(data[5].split(" ")[-1]))
        monkeys.append(monkey)
    return monkeys


def part_one():
    monkeys = get_monkeys()
    inspections = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for i, (worries, update, divisible, true_id, false_id) in enumerate(monkeys):
            while worries:
                inspections[i] += 1
                old = worries.popleft()
                worry = eval(update) // 3
                monkey_id = true_id if worry % divisible == 0 else false_id
                monkeys[monkey_id][0].append(worry)
    print(inspections)
    print(mul(*sorted(inspections)[-2:]))


def part_two():
    monkeys = get_monkeys()
    inspections = [0 for _ in range(len(monkeys))]
    special_number = reduce(mul, (x[2] for x in monkeys))
    for _ in range(10000):
        for i, (worries, update, divisible, true_id, false_id) in enumerate(monkeys):
            while worries:
                inspections[i] += 1
                old = worries.popleft()
                worry = eval(update)
                monkey_id = true_id if worry % divisible == 0 else false_id
                worry = worry % special_number
                monkeys[monkey_id][0].append(worry)
    print(inspections)
    print(mul(*sorted(inspections)[-2:]))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
