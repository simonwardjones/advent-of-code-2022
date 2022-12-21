from operator import add, sub, mul, truediv
import pathlib


def load_data():
    return pathlib.Path("inputs/day_21/data.txt").read_text().split("\n")


OPERATORS = {"+": add, "-": sub, "*": mul, "/": truediv}


def part_one():
    monkeys = dict(row.split(": ") for row in load_data())
    for monkey, exp in monkeys.items():
        monkeys[monkey] = exp.split(" ")

    def reduce(monkey):
        expression = monkeys[monkey]
        if len(expression) == 1:
            return int(expression[0])
        l, r = reduce(expression[0]), reduce(expression[2])
        return OPERATORS[expression[1]](l, r)

    print(reduce("root"))


def part_two():
    monkeys = dict(row.split(": ") for row in load_data())
    for monkey, exp in monkeys.items():
        monkeys[monkey] = exp.split(" ")

    def reduce(monkey):
        if monkey == "humn":
            return "humn"
        expression = monkeys[monkey]
        if len(expression) == 1:
            return int(expression[0])
        l, r = reduce(expression[0]), reduce(expression[2])
        if monkey == "root":
            return [l, "=", r]
        if isinstance(l, (float, int)) and isinstance(r, (float, int)):
            return OPERATORS[expression[1]](l, r)
        return [l, expression[1], r]

    root = reduce("root")
    print(root)
    l, r = root[0], root[2]
    while l != "humn" and r != "humn":
        print(l, r)
        if isinstance(r, (float, int)):
            if isinstance(l[0], (float, int)):
                if l[1] == "/":
                    l, r = l[2], l[0] / r
                elif l[1] == "*":
                    l, r = l[2], r / l[0]
                elif l[1] == "+":
                    l, r = l[2], r - l[0]
                else:
                    l, r = l[2], l[0] - r
            else:
                if l[1] == "/":
                    l, r = l[0], l[2] * r
                elif l[1] == "*":
                    l, r = l[0], r / l[2]
                elif l[1] == "+":
                    l, r = l[0], r - l[2]
                else:
                    l, r = l[0], l[2] + r
        else:
            l, r = r, l
    print(l, r)


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
