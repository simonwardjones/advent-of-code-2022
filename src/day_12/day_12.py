import pathlib
import heapq
from string import ascii_lowercase


def load_data():
    return [
        list(row)
        for row in pathlib.Path("inputs/day_12/data.txt").read_text().split("\n")
    ]


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
HEIGHT = dict(zip(ascii_lowercase, range(26))) | {"E": 25, "S": 0}


def part(stop="a"):
    elf_map = load_data()
    m, n = len(elf_map), len(elf_map[0])
    start_row = ["E" in row for row in elf_map].index(True)
    start_col = elf_map[start_row].index("E")
    start = (start_row, start_col)
    visited = set()
    visited.add(start)
    current_heads = [[0, "E", start]]
    while current_heads:
        steps, letter, (px, py) = heapq.heappop(current_heads)
        if letter == stop:
            break
        neighbours = list(
            filter(
                lambda x: x[0] in range(m)
                and x[1] in range(n)
                and x not in visited
                and HEIGHT[elf_map[x[0]][x[1]]] >= HEIGHT[letter] - 1,
                map(lambda x: (x[0] + px, x[1] + py), DIRECTIONS),
            )
        )
        for neighbour in neighbours:
            visited.add(neighbour)
            heapq.heappush(
                current_heads,
                [steps + 1, elf_map[neighbour[0]][neighbour[1]], neighbour],
            )
    print(steps, letter, (px, py))


def main():
    part("S")
    part("a")


if __name__ == "__main__":
    main()
