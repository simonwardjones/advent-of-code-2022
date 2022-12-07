import pathlib
from typing import NamedTuple, Optional


def load_data():
    return pathlib.Path("inputs/day_07/data.txt").read_text().split("\n")


class File:
    def __init__(self, name: str, size: Optional[int] = None, parent=None):
        self.name = name
        self.children = {}
        self._size = size
        self.parent = parent

    def add_child(self, name, size=None):
        self.children[name] = File(name, size, parent=self)

    def is_dir(self):
        return self._size is None

    @property
    def size(self) -> int:
        if self._size:
            return self._size
        return sum(child.size for child in self.children.values())

    def display(self, level=0):
        output = ""
        output += "  " * level + f"{self.name} ({self.size})\n"
        for child in self.children.values():
            output += child.display(level + 1)
        return output

    def walk(self, below=100000):
        for child in self.children.values():
            yield child
            yield from child.walk()

    def __repr__(self):
        return f"<File(name={self.name},size={self.size})>"


def get_root_folder():
    root = File("/")
    elf_data = load_data()
    current_folder = root
    for i, line in enumerate(elf_data):
        output = line.split(" ")
        if output[0] == "$":
            # print(f"Processing command {output[1:]}")
            if output[1] == "cd":
                if output[2] == "/":
                    current_folder = root
                elif output[2] == "..":
                    current_folder = current_folder.parent
                else:
                    # print(f"Changing dir to {output[2]}")
                    current_folder = current_folder.children[output[2]]
            if output[1] == "ls":
                # print("Listing")
                pass
        else:
            # print(f"add child {output[1]}")
            if output[0] == "dir":
                current_folder.add_child(name=output[1])
            else:
                current_folder.add_child(name=output[1], size=int(output[0]))
    return root


def part_one():
    root = get_root_folder()
    # print(root.display())
    total = 0
    for file in root.walk():
        if file.size < 100000 and file.is_dir():
            total += file.size
    print(total)


def part_two():
    root = get_root_folder()

    unused = 70000000 - root.size
    to_clear = 30000000 - unused

    to_delete = root
    for file in root.walk():
        if file.size > to_clear and file.is_dir() and file.size < to_delete.size:
            to_delete = file
    print(to_delete)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
