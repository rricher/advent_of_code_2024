import sys
import re

sys.path.insert(0, "/Users/ryan/Projects/advent_of_code")

from read_file import get_input

# Start 1:38
# Same as p1 just have to run more cycles

cyc_2_add = {}


def process_input(input: list[str]) -> list[str]:
    stones = input[0].split(" ")
    return stones


def stone_rules(stone: str) -> str | list[str, str]:
    if stone == "0":
        return "1"
    elif len(stone) % 2 == 0:
        # print(stone, len(stone), len(stone) / 2)
        first_stone = stone[: int(len(stone) / 2)]
        # print(first_stone)
        second_stone = stone[int(len(stone) / 2) :]
        second_stone = re.sub("^0+", "", second_stone)
        if not second_stone:
            second_stone = "0"
        # print(second_stone)
        stone = [first_stone, second_stone]
    else:
        stone = str(int(stone) * 2024)
    return stone


def multiply_stones(cycles: int, stones: list[str]) -> list[str]:
    for i in range(cycles):
        temp_stones = []
        zeros = []
        for j in range(len(stones)):
            stone = stones[j]
            if stone == "0":
                left = cycles - i
                if left not in cyc_2_add:
                    cyc_2_add[left] = 0
                cyc_2_add[left] += 1
                zeros.append(j)
            else:
                stone = stone_rules(stone)
                if type(stone) is list:
                    temp_stones.append(stone[0])
                    temp_stones.append(stone[1])
                else:
                    temp_stones.append(stone)
        for j in range(len(zeros) - 1, -1, -1):
            temp_stones.pop(zeros[j])
        stones = temp_stones
        # print(stones)
    return stones, cyc_2_add


def main() -> None:
    # input = get_input("./input.txt")
    # stones = process_input(input)
    stones = ["125", "17"]
    stones, cyc_2_add = multiply_stones(55, stones)
    print(len(stones))
    print(cyc_2_add)


if __name__ == "__main__":
    main()
