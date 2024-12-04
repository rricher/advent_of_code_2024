import re
from day_4.read_file import get_input


def uncorrupt(corrupted):
    total = 0
    do = True
    for line in corrupted:
        pattern = re.compile(r"do\(\)|don\'t\(\)|mul\(\d+\,\d+\)")
        mults = pattern.findall(line)
        for mult in mults:
            if mult == "do()":
                do = True
            elif mult == "don't()":
                do = False
            else:
                mult = re.findall(r"(\d+)\,(\d+)", mult)[0]
            if type(mult) is tuple and do:
                total += int(mult[0]) * int(mult[1])
    print(total)


def main() -> None:
    corrupted = get_input()
    uncorrupt(corrupted)


if __name__ == "__main__":
    main()
