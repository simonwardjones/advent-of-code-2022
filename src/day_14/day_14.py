import pathlib


def load_data():
    return pathlib.Path("inputs/day_14/sample_data.txt").read_text().split("\n")


def sign(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    return -1


def create_map():
    paths = []
    map_points = {}
    for line in load_data():
        paths.append([list(map(int, pair.split(","))) for pair in line.split(" -> ")])
    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            # print(f"Generate path from {(x1, y1)} to {(x2, y2)}")
            if y1 == y2:
                for i in range(abs(x2 - x1) + 1):
                    map_points[(x1 + i * sign(x1, x2), y1)] = "#"
            else:
                for i in range(abs(y2 - y1) + 1):
                    map_points[(x1, y1 + i * sign(y1, y2))] = "#"
    return map_points


def get_next_point(sand_at, map_points):
    x, y = sand_at
    if (x, y + 1) not in map_points:
        return (x, y + 1)
    elif (x - 1, y + 1) not in map_points:
        return (x - 1, y + 1)
    elif (x + 1, y + 1) not in map_points:
        return (x + 1, y + 1)


def part_one():
    map_points = create_map()
    max_map = max(point[1] for point in map_points)
    source = sand_at = (500, 0)
    while sand_at[1] < max_map:
        next_point = get_next_point(sand_at, map_points)
        if next_point is None:
            map_points[sand_at] = "."
            sand_at = source
        else:
            sand_at = next_point
    # print(map_points)
    print(sum(1 for x in map_points.values() if x == "."))


def part_two():
    map_points = create_map()
    max_map = max(point[1] for point in map_points)
    floor = max_map + 2
    print(min(point[0] for point in map_points), max(point[0] for point in map_points))
    for x in range(-700, 1200):
        map_points[(x, floor)] = "#"
    source = sand_at = (500, 0)
    while sand_at[1] < floor:
        next_point = get_next_point(sand_at, map_points)
        if next_point is None:
            if sand_at == source:
                map_points[sand_at] = "."
                break
            map_points[sand_at] = "."
            sand_at = source
        else:
            sand_at = next_point
    # print(map_points)
    print(sum(1 for x in map_points.values() if x == "."))


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
