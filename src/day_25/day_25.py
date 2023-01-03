import pathlib


def load_data():
    return pathlib.Path("inputs/day_25/data.txt").read_text().splitlines()


def from_snafu(snafu):
    fuel = 0
    for i, number in enumerate(reversed(snafu)):
        if number == "=":
            number = -2
        elif number == "-":
            number = -1
        else:
            number = int(number)
        fuel += (5**i) * number
    return fuel


def to_snafu(number):
    snafu = ""
    power = 1
    base = 5**power
    while True:
        base = 5**power
        quotient, remainder = divmod(number, base)
        if quotient == 0 and remainder == 0:
            break
        remainder = remainder // (5 ** (power - 1))
        if remainder in [3, 4]:
            remainder -= 5
        number = number - (remainder * (5 ** (power - 1)))
        if remainder == -2:
            value = "="
        elif remainder == -1:
            value = "-"
        else:
            value = str(remainder)
        snafu = value + snafu
        power += 1
    return snafu


def part_one():
    fuel_requirements = load_data()
    total = 0
    for balloon in fuel_requirements:
        fuel = from_snafu(balloon)
        total += fuel
    print(total)
    print(to_snafu(total))


def main():
    part_one()


if __name__ == "__main__":
    main()
