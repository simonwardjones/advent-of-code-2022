import pathlib
import re
from collections import defaultdict, deque
from typing import NamedTuple
import time

startTime = time.time()

#####your python script#####


def load_data():
    return [
        (r[0], r[1:], int(re.findall(r"\d+", row).pop()))
        for row in pathlib.Path("inputs/day_16/data.txt").read_text().split("\n")
        for r in [re.findall(r"[A-Z]{2}", row)]
    ]


class Path(NamedTuple):
    current_node: str
    last_visited: dict[str, int]
    time: int
    rate: int
    flow: int
    full_path: str


def part_one():
    valves = load_data()
    n_nodes = len(valves)
    distances = {}
    siblings = dict(v[0:2] for v in valves)
    points = dict(v[::2] for v in valves)
    nearest_pointed_neighbours = defaultdict(list)
    while len(distances) < ((n_nodes**2) - n_nodes):
        for i, (start, neighbours, flow) in enumerate(valves):
            visited = set([start])
            to_visit = deque()
            for nn in neighbours:
                to_visit.append((nn, 1, 0))
            while to_visit:
                neighbour, distance, n_flow = to_visit.popleft()
                visited.add(neighbour)
                distances[(start, neighbour)] = distance
                if n_flow == 0 and points[neighbour]:
                    nearest_pointed_neighbours[start].append(neighbour)
                for nn in siblings[neighbour]:
                    if nn in visited:
                        continue
                    to_visit.append((nn, distance + 1, n_flow + points[neighbour]))
    pointers = [k for k, v in points.items() if v]

    paths = deque([Path("AA", {}, 0, 0, 0, "AA")])  # at the end of time period
    complete_paths = []
    while paths:
        path = paths.popleft()
        if len(path.last_visited) == len(pointers):
            complete_paths.append(
                (path.flow + path.rate * (30 - path.time), path.full_path)
            )
            continue
        for nn in pointers:
            if nn == path.current_node:
                continue

            if nn in path.last_visited:
                continue

            distance = distances[(path.current_node, nn)]
            if (path.time + distance) >= 30:
                complete_paths.append(
                    (path.flow + path.rate * (30 - path.time), path.full_path)
                )
                continue

            new_distance = distance + 1
            tracking = dict(path.last_visited)
            tracking[nn] = True
            paths.append(
                Path(
                    nn,
                    tracking,
                    path.time + new_distance,
                    path.rate + points[nn],
                    path.flow + (path.rate * new_distance),
                    path.full_path + nn,
                )
            )
    print(max(complete_paths))


def part_two():
    valves = load_data()
    n_nodes = len(valves)
    distances = {}
    siblings = dict(v[0:2] for v in valves)
    points = dict(v[::2] for v in valves)
    nearest_pointed_neighbours = defaultdict(list)
    while len(distances) < ((n_nodes**2) - n_nodes):
        for i, (start, neighbours, flow) in enumerate(valves):
            visited = set([start])
            to_visit = deque()
            for nn in neighbours:
                to_visit.append((nn, 1, 0))
            while to_visit:
                neighbour, distance, n_flow = to_visit.popleft()
                visited.add(neighbour)
                distances[(start, neighbour)] = distance
                if n_flow == 0 and points[neighbour]:
                    nearest_pointed_neighbours[start].append(neighbour)
                for nn in siblings[neighbour]:
                    if nn in visited:
                        continue
                    to_visit.append((nn, distance + 1, n_flow + points[neighbour]))

    pointers = [k for k, v in points.items() if v]

    paths = deque([Path("AA", {}, 0, 0, 0, "AA")])  # at the end of time period
    complete_paths = []
    pointers_filtered = [
        p for p in pointers if p not in {"EI", "OA", "EK", "YP", "PU", "ZO"}
    ]

    while paths:
        path = paths.popleft()
        for nn in pointers_filtered:
            if nn == path.current_node:
                continue
            if nn in path.last_visited and path.last_visited[nn] == path.rate:
                continue

            distance = distances[(path.current_node, nn)]
            if (path.time + distance) >= 26 or len(path.last_visited) == 14:
                complete_paths.append(
                    (path.flow + path.rate * (26 - path.time), path.full_path)
                )
                continue

            new_rate = path.rate
            if nn not in path.last_visited:
                tracking = dict(path.last_visited)
                new_rate = path.rate + points[nn]
                tracking[nn] = new_rate
                new_distance = distance + 1
                paths.append(
                    Path(
                        nn,
                        tracking,
                        path.time + new_distance,
                        new_rate,
                        path.flow + (path.rate * new_distance),
                        path.full_path + nn,
                    )
                )
            # print(complete_paths)
    # print(distances)
    # print(complete_paths[-10:])
    # print(max(complete_paths))
    print(max(complete_paths)[0] + 1592)


def main():
    part_one()
    # part_two()


if __name__ == "__main__":
    main()

executionTime = time.time() - startTime
print("Execution time in seconds: " + str(executionTime))
