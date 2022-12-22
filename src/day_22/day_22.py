import pathlib


def load_data():
    raw_map, raw_instructions = (
        pathlib.Path("inputs/day_22/data.txt").read_text().split("\n\n")
    )
    raw_map = raw_map.split("\n")
    M, N = len(raw_map), max(len(row) for row in raw_map)
    map = [
        [row[i] if i < len(row) and row[i] != " " else None for i in range(N)]
        for row in raw_map
    ]
    instructions, cur = [], ""
    for x in raw_instructions:
        if x in ("R", "L"):
            if cur:
                instructions.append(int(cur))
                cur = ""
            instructions.append(x)
        elif x.isdigit():
            cur += x
    instructions.append(int(cur))
    return map, instructions


# right, down, left, up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_one():
    map, instructions = load_data()
    M, N = len(map), len(map[0])
    y, x = next(
        filter(
            lambda x: map[x[0]][x[1]] == ".",
            ((row, col) for row in range(M) for col in range(M)),
        )
    )
    current_direction_index, (dy, dx) = 0, DIRECTIONS[0]
    for instruction in instructions:
        if instruction in ("R", "L"):
            current_direction_index = (
                current_direction_index + (1 if instruction == "R" else -1)
            ) % 4
            (dy, dx) = DIRECTIONS[current_direction_index]
        else:
            for _ in range(instruction):
                (try_y, try_x) = ((y + dy) % M, (x + dx) % N)
                while not map[try_y][try_x]:
                    (try_y, try_x) = ((try_y + dy) % M, (try_x + dx) % N)
                if map[try_y][try_x] == "#":
                    break
                y, x = try_y, try_x
    row, col = y + 1, x + 1
    print(1000 * row + 4 * col + current_direction_index)


# my map
"""
  .##
  .#.
  ##.
  #..
"""

# right, down, left, up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_two():
    map, instructions = load_data()
    M, N = len(map), len(map[0])
    y, x = next(
        filter(
            lambda x: map[x[0]][x[1]] == ".",
            ((row, col) for row in range(M) for col in range(M)),
        )
    )
    current_direction_index, (dy, dx), face = 0, DIRECTIONS[0], 1
    for instruction in instructions:
        if instruction in ("R", "L"):
            current_direction_index = (
                current_direction_index + (1 if instruction == "R" else -1)
            ) % 4
            dy, dx = DIRECTIONS[current_direction_index]
        else:
            for _ in range(instruction):
                if not map[y][x]:
                    print(f"Warning gone off {y, x}")
                    exit(0)
                face = (y // 50 * 3) + (x // 50)
                if y == 0 and dy == -1 and face == 1:
                    try_y, try_x, try_index = x + 100, 0, 0  # right
                elif x == 50 and dx == -1 and face == 1:
                    try_y, try_x, try_index = 149 - y, 0, 0
                elif y == 0 and dy == -1 and face == 2:
                    try_y, try_x, try_index = 199, x - 100, 3
                elif x == 149 and dx == 1 and face == 2:
                    try_y, try_x, try_index = 150 - y - 1, 99, 2
                elif y == 49 and dy == 1 and face == 2:
                    try_y, try_x, try_index = x - 50, 99, 2
                elif x == 99 and dx == 1 and face == 4:
                    try_y, try_x, try_index = 49, y + 50, 3
                elif x == 50 and dx == -1 and face == 4:
                    try_y, try_x, try_index = 100, y - 50, 1
                elif y == 100 and dy == -1 and face == 6:
                    try_y, try_x, try_index = x + 50, 50, 0
                elif x == 0 and dx == -1 and face == 6:
                    try_y, try_x, try_index = 149 - y, 50, 0
                elif x == 99 and dx == 1 and face == 7:
                    try_y, try_x, try_index = 149 - y, 149, 2
                elif y == 149 and dy == 1 and face == 7:
                    try_y, try_x, try_index = 100 + x, 49, 2
                elif x == 0 and dx == -1 and face == 9:
                    try_y, try_x, try_index = 0, y - 100, 1
                elif y == 199 and dy == 1 and face == 9:
                    try_y, try_x, try_index = 0, x + 100, 1
                elif x == 49 and dx == 1 and face == 9:
                    try_y, try_x, try_index = 149, y - 100, 3
                else:
                    try_y, try_x, try_index = y + dy, x + dx, current_direction_index
                if map[try_y][try_x] == "#":
                    break
                y, x = try_y, try_x
                current_direction_index = try_index
                dy, dx = DIRECTIONS[try_index]
    row, col = y + 1, x + 1
    print(1000 * row + 4 * col + current_direction_index)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
