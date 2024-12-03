import re


def fileinput():
    corrupted = []
    with open("./input.txt", "r") as file:
        for line in file:
            corrupted.append(line)
    return corrupted


def uncorrupt(corrupted):
    total = 0
    for line in corrupted:
        pattern = re.compile(r"mul\((\d+),(\d+)\)")
        mults = pattern.findall(line)
        for mult in mults:
            total += int(mult[0]) * int(mult[1])
    print(total)


def main() -> None:
    corrupted = fileinput()
    uncorrupt(corrupted)


if __name__ == "__main__":
    main()
