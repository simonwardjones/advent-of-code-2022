from functools import reduce
from itertools import product
from operator import mul
import pathlib


def load_data():
    return pathlib.Path("inputs/day_08/data.txt").read_text()

# filthy answers.

def part_one():
    elf_data = [[int(number) for number in row] for row in load_data().split("\n")]
    n_rows = len(elf_data)
    n_cols = len(elf_data[0])
    visible = {
        (i, j): [True] * 4 for i in range(n_rows) for j in range(n_cols)
    }  # left up right down
    max_left = [-1] * n_cols
    max_up = [-1] * n_rows
    max_right = [-1] * n_cols
    max_down = [-1] * n_rows
    for i, row in enumerate(elf_data):
        for j, value in enumerate(row):
            if value <= max_left[i]:
                visible[(i, j)][0] = False
            else:
                max_left[i] = value
            if value <= max_up[j]:
                visible[(i, j)][1] = False
            else:
                max_up[j] = value
    for i, row in enumerate(reversed(elf_data)):
        for j, value in enumerate(reversed(row)):
            if value <= max_right[i]:
                visible[(n_rows - 1 - i, n_rows - 1 - j)][2] = False
            else:
                max_right[i] = value
            if value <= max_down[j]:
                visible[(n_rows - 1 - i, n_rows - 1 - j)][3] = False
            else:
                max_down[j] = value

    print(sum(1 for checks in visible.values() if any(checks)))


def part_two():
    elf_data = [[int(number) for number in row] for row in load_data().split("\n")]
    n_rows = len(elf_data)
    n_cols = len(elf_data[0])
    scenic_scores = {(i, j): [1] * 4 for i in range(n_rows) for j in range(n_cols)}
    for i, j in product(range(n_rows), range(n_cols)):
        print(f"Checking {i,j, elf_data[i][j]}")
        left_step = up_step = right_step = down_step = 0
        for x in range(j - 1, -1, -1):
            left_step += 1
            if elf_data[i][j] <= elf_data[i][x]:
                break
        scenic_scores[(i, j)][0] = left_step
        for x in range(i - 1, -1, -1):
            up_step += 1
            if elf_data[i][j] <= elf_data[x][j]:
                break
        scenic_scores[(i, j)][1] = up_step
        for x in range(j + 1, n_cols):
            right_step += 1
            if elf_data[i][j] <= elf_data[i][x]:
                break
        scenic_scores[(i, j)][2] = right_step
        for x in range(i + 1, n_cols):
            down_step += 1
            if elf_data[i][j] <= elf_data[x][j]:
                break
        scenic_scores[(i, j)][3] = down_step
    print(scenic_scores)
    print(max(reduce(mul, scores) for scores in scenic_scores.values()))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
