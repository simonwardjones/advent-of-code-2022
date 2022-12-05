import pathlib
import re
from queue import LifoQueue


def load_data():
    return pathlib.Path("inputs/day_05/data.txt").read_text().split("\n\n")


def part_one():
    raw_stacks, moves = load_data()
    print(raw_stacks)
    stacks = raw_stacks.split("\n")[:-1][::-1]
    moves = [[int(x) for x in re.findall(r"\d+", line)] for line in moves.split("\n")]
    n_stacks = (len(stacks[0]) + 1) // 4
    queues = [[] for _ in range(n_stacks)]
    for line in stacks:
        for stack_id in range(n_stacks):
            if line[stack_id * 4 + 1] != " ":
                queues[stack_id].append(line[stack_id * 4 + 1])
    for move, from_, to in moves:
        for _ in range(move):
            queues[to - 1].append(queues[from_ - 1].pop())
    print("".join(queue[-1] for queue in queues))


def part_two():
    raw_stacks, moves = load_data()
    stacks = raw_stacks.split("\n")[:-1][::-1]
    moves = [[int(x) for x in re.findall(r"\d+", line)] for line in moves.split("\n")]
    n_stacks = (len(stacks[0]) + 1) // 4
    queues = [[] for _ in range(n_stacks)]
    for line in stacks:
        for stack_id in range(n_stacks):
            if line[stack_id * 4 + 1] != " ":
                queues[stack_id].append(line[stack_id * 4 + 1])
    for move, from_, to in moves:
        queues[to - 1].extend(queues[from_ - 1][-move:])
        queues[from_ - 1] = queues[from_ - 1][:-move]
    print("".join(queue[-1] for queue in queues))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
