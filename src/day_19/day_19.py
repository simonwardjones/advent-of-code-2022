from collections import deque
from functools import cache, reduce
from itertools import starmap
from operator import mul
import pathlib
import re


def load_data():
    return [
        list(map(int, re.findall(r"\d+", row)[1:]))
        for row in pathlib.Path("inputs/day_19/sample_data.txt").read_text().split("\n")
    ]


def part_one():
    blueprints = load_data()
    found = []
    T = 32
    for blueprint in blueprints[:3]:
        (
            o_o,
            c_o,
            s_o,
            s_c,
            g_o,
            g_s,
        ) = blueprint
        print(f"{blueprint=}")
        # ore, clay, obsidian, geode
        to_check = deque([(1, 0, 0, 0, 0, 0, 0, 0, T)])
        # 1. Select robots to by, decrease bank
        # 2. Increase bank from robots
        # 3. Increase robots
        # print(f"{robots_bank=}, {time_left=}")
        seen = set()
        max_seen = 0
        R = (
            max(
                o_o,
                c_o,
                s_o,
                g_o,
                s_c,
                g_s,
            )*2
        )
        print(R)
        while to_check:
            o_r, c_r, s_r, g_r, o, c, s, g, t = to_check.popleft()
            # print(state)
            if (o_r, c_r, s_r, g_r, o, c, s, g) in seen:
                continue
            seen.add((o_r, c_r, s_r, g_r, o, c, s, g))

            if t == 0:
                if g > max_seen:
                    max_seen = g
                continue

            o = min(R, o)
            c = min(R, c)
            s = min(R, s)
            if o >= g_o and s >= g_s:
                # Always building it
                to_check.append(
                    (
                        o_r,
                        c_r,
                        s_r,
                        g_r + 1,
                        o - g_o + o_r,
                        c + c_r,
                        s - g_s + s_r,
                        g + g_r,
                        t - 1,
                    )
                )
                continue

            if o >= s_o and c >= s_c and s_r < g_s:
                to_check.append(
                    (
                        o_r,
                        c_r,
                        s_r + 1,
                        g_r,
                        o - s_o + o_r,
                        c - s_c + c_r,
                        s + s_r,
                        g + g_r,
                        t - 1,
                    )
                )

            if o >= c_o and c_r < s_c:  # don't make s if already making enough
                to_check.append(
                    (
                        o_r,
                        c_r + 1,
                        s_r,
                        g_r,
                        o - c_o + o_r,
                        c + c_r,
                        s + s_r,
                        g + g_r,
                        t - 1,
                    )
                )

            if o >= o_o and o_r < max(o_o, c_o, s_o, g_o):
                to_check.append(
                    (
                        o_r + 1,
                        c_r,
                        s_r,
                        g_r,
                        o - o_o + o_r,
                        c + c_r,
                        s + s_r,
                        g + g_r,
                        t - 1,
                    )
                )

            to_check.append(
                (
                    o_r,
                    c_r,
                    s_r,
                    g_r,
                    o + o_r,
                    c + c_r,
                    s + s_r,
                    g + g_r,
                    t - 1,
                )
            )
        found.append(max_seen)
    print(found)
    print(reduce(mul, found))


def main():
    part_one()


if __name__ == "__main__":
    main()
