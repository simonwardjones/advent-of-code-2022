import pathlib


def load_data():
    return [
        int(row)
        for row in pathlib.Path("inputs/day_20/data.txt").read_text().split("\n")
    ]


def part_one():
    elf_data = [x * 811589153 for x in load_data()]
    N = len(elf_data)
    numbers = elf_data[:]
    print(f"{N=} {len(set(numbers))=}") 
    locations = list(range(N))
    for _ in range(10):
        for i in range(N):
            number = elf_data[i]
            number_location = locations.index(i)
            location = number_location % (N - 1)
            del numbers[number_location]
            del locations[number_location]
            location = (location + number) % (N - 1)
            if location == 0:
                location = N
            numbers.insert(location, number)
            locations.insert(location, i)
    start = numbers.index(0)
    total = 0
    for diff in [1000, 2000, 3000]:
        location = (start + diff) % N
        total += numbers[location]
    print(total)


def part_two():
    elf_data = load_data()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
