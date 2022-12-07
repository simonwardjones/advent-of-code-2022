import pathlib
import sys

DAY_TEMPLATE = """import pathlib


def load_data():
    return pathlib.Path("inputs/day_{day:02}/sample_data.txt").read_text()


def part_one():
    elf_data = load_data()
    print(elf_data)


def part_two():
    elf_data = load_data()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
"""


def make_day(day):
    if not day:
        print("Pass day number command line argument")
        return
    pathlib.Path(f"src/day_{day:02}").mkdir(exist_ok=True)
    pathlib.Path(f"inputs/day_{day:02}").mkdir(exist_ok=True)
    if not pathlib.Path(f"src/day_{day:02}/day_{day:02}.py").exists():
        pathlib.Path(f"src/day_{day:02}/day_{day:02}.py").write_text(
            DAY_TEMPLATE.format(day=day)
        )
    if not pathlib.Path(f"inputs/day_{day:02}/data.txt").exists():
        pathlib.Path(f"inputs/day_{day:02}/data.txt").touch()
    if not pathlib.Path(f"inputs/day_{day:02}/sample_data.txt").exists():
        pathlib.Path(f"inputs/day_{day:02}/sample_data.txt").touch()


if __name__ == "__main__":
    day = None
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
    print(f"{day=}")
    make_day(day=day)
