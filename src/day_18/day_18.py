from collections import deque
from operator import itemgetter
import pathlib


def load_data():
    return [
        tuple(int(item) for item in row.split(","))
        for row in pathlib.Path("inputs/day_18/sample_data.txt").read_text().split("\n")
    ]


def part_one():
    lava_cubes = load_data()
    print(
        sum(
            6
            - sum(
                1 if abs(cx - nx) + abs(cy - ny) + abs(cz - nz) == 1 else 0
                for (nx, ny, nz) in lava_cubes
            )
            for (cx, cy, cz) in lava_cubes
        )
    )


NEIGHBOURS = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]


def part_two():
    lava_cubes = load_data()
    total_sides = 0
    mx, Mx, my, My, mz, Mz = [
        f(cube[i] for cube in lava_cubes)
        for i in [0, 1, 2]
        for f in [lambda x: min(x) - 1, lambda x: max(x) + 1]
    ]
    nodes = deque([(mx, my, mz)])
    visited = set()
    while nodes:
        x, y, z = nodes.popleft()
        for dx, dy, dz in NEIGHBOURS:
            (px, py, pz) = point = (x + dx, y + dy, z + dz)
            if not (mx <= px <= Mx and my <= py <= My and mz <= pz <= Mz):
                continue
            if point in lava_cubes:
                total_sides += 1
                continue
            if point not in visited:
                nodes.append(point)
                visited.add(point)
    print(total_sides)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
