import pathlib

DIRECTIONS = {"R": (0, 1), "U": (1, 0), "L": (0, -1), "D": (-1, 0)}


def load_data():
    return [
        (DIRECTIONS[row[0]], int(row[2:]))
        for row in pathlib.Path("inputs/day_09/data.txt").read_text().split("\n")
    ]


def add_direction(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def sign(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def update_tail(tail, head):
    if (abs(tail[0] - head[0]) < 2) and (abs(tail[1] - head[1]) < 2):
        return tail
    return (tail[0] + sign(head[0], tail[0]), tail[1] + sign(head[1], tail[1]))


def part_one():
    motions = load_data()
    head = tail = (0, 0)
    visited = set()
    for direction, steps in motions:
        for _ in range(steps):
            head = add_direction(head, direction)
            tail = update_tail(tail, head)
            visited.add(tail)
    print(len(visited))


def part_two():
    motions = load_data()
    knots = [(0, 0)] * 10
    visited = set()
    for direction, steps in motions:
        for _ in range(steps):
            knots[0] = add_direction(knots[0], direction)
            for i in range(1, 10):
                knots[i] = update_tail(knots[i], knots[i - 1])
            visited.add(knots[-1])
    print(len(visited))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
