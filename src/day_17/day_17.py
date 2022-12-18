from itertools import cycle
import pathlib

SHAPES_STR = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""
SHAPES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, -1), (1, 0), (1, -1), (1, -2), (2, -1)],
    [(2, 0), (2, -1), (2, -2), (1, -2), (0, -2)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (1, 0), (0, -1), (1, -1)],
]

SHAPE_HEIGHTS = [
    max(point[1] for point in shape) - min(point[1] for point in shape) + 1
    for shape in SHAPES
]


def load_data():
    return pathlib.Path("inputs/day_17/data.txt").read_text()


def bound(point):
    x, y = point
    if x == 0 or x == 8 or y == 0:
        return True


def part_one():
    jet_pattern = list(map(lambda x: 1 if x == ">" else -1, load_data()))
    # print(jet_pattern)
    # print(SHAPES)
    # print(SHAPE_HEIGHTS)
    placed_points = {}
    placed_shapes = 0
    shape_heights = cycle(zip(SHAPES, SHAPE_HEIGHTS))
    jets = cycle(jet_pattern)
    max_height = 0  # start at the floor
    jet_pattern_len = len(jet_pattern)
    print(f"{jet_pattern_len=}")
    jets_seen = 0
    prev_mh = 0
    while placed_shapes < 5601:
        shape, shape_height = next(shape_heights)
        top_left = (3, max_height + 3 + shape_height)
        if jets_seen % (jet_pattern_len * 1) == 0:
            print((placed_shapes - 1724) /  1725,max_height, max_height - prev_mh)
            prev_mh = max_height
        if placed_shapes ==  1724 + 1601:
            print("HEIGHT", max_height, max_height - 2613)
            exit
        shape_placed = False
        while not shape_placed:
            # wind
            jet = next(jets)
            jets_seen += 1
            tpx, tpy = top_left[0] + jet, top_left[1]
            if all(
                (not bound(point)) and point not in placed_points
                for point in [(tpx + x, tpy + y) for x, y in shape]
            ):
                top_left = (tpx, tpy)
            tpx, tpy = top_left[0], top_left[1] - 1
            if all(
                not bound(point) and point not in placed_points
                for point in [(tpx + x, tpy + y) for x, y in shape]
            ):
                top_left = (tpx, tpy)
            else:
                for x, y in [top_left]:
                    for dx, dy in shape:
                        max_height = max(max_height, y + dy)
                        placed_points[(x + dx, y + dy)] = True
                shape_placed = True
        # print(shape, shape_height)
        placed_shapes += 1
    print(f"{jets_seen=}")
    print(placed_shapes)
    print(max(k[1] for k in placed_points))

def part_two():
    elf_data = load_data()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()


579710143 * 2630 + 2613 + 2426