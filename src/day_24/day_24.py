from collections import defaultdict, deque
import pathlib


def load_data():
    return [
        list(row)
        for row in pathlib.Path("inputs/day_24/sample_data.txt").read_text().split("\n")
    ]


OPTIONS = [
    (1, 0),
    (0, 1),
    (0, 0),
    (-1, 0),
    (0, -1),
]

DIRECTIONS = {"v": (1, 0), ">": (0, 1), "^": (-1, 0), "<": (0, -1)}


def part_one():
    pos = (-1, 0)
    storm_map = defaultdict(list)
    flat_map = load_data()
    M, N = len(flat_map) - 2, len(flat_map[0]) - 2
    # state steps, pos
    routes = deque([(0, [pos])])
    for row, values in enumerate(flat_map):
        for col, value in enumerate(values):
            if value in DIRECTIONS:
                storm_map[(row - 1, col - 1)].append(value)
    best = (float("inf"), (M, N))
    STEPS = -1
    seen = {}
    max_progress = 0
    while routes:
        # check for winner
        steps, [*_, (pos_x, pos_y)] = state = routes.popleft()
        pos = (pos_x, pos_y)

        if pos_x + pos_y < max_progress - 15:
            continue
        max_progress = max(max_progress, pos_x, pos_y)

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] < steps - 10:
            continue

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] == steps:
            continue

        seen[(pos_x, pos_y)] = steps

        # print(state)
        if pos_x == M - 1 and pos_y == N - 1 and steps < best[0]:
            best = state
            print(f"{state[0]=}")
            break

        if steps > M * N:
            continue
        # create the new map if we ar onto the next
        if steps > STEPS:
            STEPS += 1
            print(STEPS)
            new_storm_map = defaultdict(list)
            for (px, py), points in storm_map.items():
                for point in points:
                    for dx, dy in [DIRECTIONS[point]]:
                        new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
            storm_map = new_storm_map

        # find options.
        for dx, dy in OPTIONS:
            new_pos = (pos_x + dx, pos_y + dy)
            if (
                (0 <= new_pos[0] <= M - 1 and 0 <= new_pos[1] <= N - 1)
                or STEPS < 3
                and dx == dy == 0
            ) and new_pos not in storm_map:
                routes.append((steps + 1, [*_, pos, new_pos]))
        # print()
        # print(storm_map)


def part_two():
    pos = (-1, 0)
    storm_map = defaultdict(list)
    flat_map = load_data()
    M, N = len(flat_map) - 2, len(flat_map[0]) - 2
    # state steps, pos
    routes = deque([(0, [pos])])
    for row, values in enumerate(flat_map):
        for col, value in enumerate(values):
            if value in DIRECTIONS:
                storm_map[(row - 1, col - 1)].append(value)
    best = (float("inf"), (M, N))
    STEPS = -1
    seen = {}
    max_progress = 0
    while routes:
        # check for winner
        steps, [*_, (pos_x, pos_y)] = state = routes.popleft()
        pos = (pos_x, pos_y)

        if pos_x + pos_y < max_progress - 15:
            continue
        max_progress = max(max_progress, pos_x + pos_y)

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] < steps - 10:
            continue

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] == steps:
            continue

        seen[(pos_x, pos_y)] = steps

        if pos_x == M - 1 and pos_y == N - 1 and steps < best[0]:
            best = state
            print(f"{state[0]=}")
            break

        if steps > M * N:
            continue
        # create the new map if we ar onto the next
        if steps > STEPS:
            STEPS += 1
            new_storm_map = defaultdict(list)
            for (px, py), points in storm_map.items():
                for point in points:
                    for dx, dy in [DIRECTIONS[point]]:
                        new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
            storm_map = new_storm_map

        # find options.
        for dx, dy in OPTIONS:
            new_pos = (pos_x + dx, pos_y + dy)
            if (
                (0 <= new_pos[0] <= M - 1 and 0 <= new_pos[1] <= N - 1)
                or STEPS < 3
                and dx == dy == 0
            ) and new_pos not in storm_map:
                routes.append((steps + 1, [*_, pos, new_pos]))

    new_storm_map = defaultdict(list)
    for (px, py), points in storm_map.items():
        for point in points:
            for dx, dy in [DIRECTIONS[point]]:
                new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
    storm_map = new_storm_map

    steps, [*_, (pos_x, pos_y)]
    steps = 0
    new_routes = deque([(steps, [(pos_x + 1, pos_y)])])

    STEPS = -1
    seen = {}
    max_progress = M + N
    while new_routes:
        # check for winner
        steps, [*_, (pos_x, pos_y)] = state = new_routes.popleft()
        pos = (pos_x, pos_y)

        if pos_x + pos_y > max_progress + 15:
            continue
        max_progress = min(max_progress, pos_x + pos_y)

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] < steps - 10:
            continue

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] == steps:
            continue

        seen[(pos_x, pos_y)] = steps

        if pos_x == 0 and pos_y == 0:
            best = state
            print(f"{state[0]=}")
            break

        if steps > M * N:
            continue
        # create the new map if we ar onto the next
        if steps > STEPS:
            STEPS += 1
            new_storm_map = defaultdict(list)
            for (px, py), points in storm_map.items():
                for point in points:
                    for dx, dy in [DIRECTIONS[point]]:
                        new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
            storm_map = new_storm_map

        # find options.
        for dx, dy in OPTIONS:
            new_pos = (pos_x + dx, pos_y + dy)
            if (
                (0 <= new_pos[0] <= M - 1 and 0 <= new_pos[1] <= N - 1)
                or new_pos in [(-1, 0), (M, N - 1)]
            ) and new_pos not in storm_map:
                new_routes.append((steps + 1, [*_, pos, new_pos]))

    # 3 lol
    new_storm_map = defaultdict(list)
    for (px, py), points in storm_map.items():
        for point in points:
            for dx, dy in [DIRECTIONS[point]]:
                new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
    storm_map = new_storm_map

    steps, [*_, (pos_x, pos_y)]
    steps = 0
    new_routes = deque([(steps, [(pos_x - 1, pos_y)])])

    STEPS = -1
    seen = {}
    max_progress = M + N
    while new_routes:
        # check for winner
        steps, [*_, (pos_x, pos_y)] = state = new_routes.popleft()
        pos = (pos_x, pos_y)

        # if pos_x + pos_y < max_progress - 40:
        #     print("this")
        #     continue
        # max_progress = max(max_progress, pos_x + pos_y)

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] < steps - 15:
            continue

        if (pos_x, pos_y) in seen and seen[(pos_x, pos_y)] == steps:
            continue

        seen[(pos_x, pos_y)] = steps

        if pos_x == M - 1 and pos_y == N - 1:
            best = state
            print(f"{state[0]=}")
            break

        if steps > M * N:
            continue
        # create the new map if we ar onto the next
        if steps > STEPS:
            STEPS += 1
            new_storm_map = defaultdict(list)
            for (px, py), points in storm_map.items():
                for point in points:
                    for dx, dy in [DIRECTIONS[point]]:
                        new_storm_map[((px + dx) % M, (py + dy) % N)].append(point)
            storm_map = new_storm_map

        # find options.
        for dx, dy in OPTIONS:
            new_pos = (pos_x + dx, pos_y + dy)
            if (
                (0 <= new_pos[0] <= M - 1 and 0 <= new_pos[1] <= N - 1)
                or new_pos in [(-1, 0), (M, N - 1)]
            ) and new_pos not in storm_map:
                new_routes.append((steps + 1, [*_, pos, new_pos]))


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
