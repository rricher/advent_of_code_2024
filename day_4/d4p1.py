import sys

sys.path.insert(0, "C:/Users/ryan/Projects/advent_of_code")

from read_file import get_input


def check_search(search):
    word = "XMAS"
    found = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            if search[i][j] == word[0]:
                found += check_surroundings(search, i, j, word)
    print(found)


def check_surroundings(search, row, col, word):
    found = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            passed = check_line(search, row, col, i, j, word)
            if passed:
                found += 1
    return found


def check_line(search, row, col, i, j, word, position=1) -> bool:
    try:
        check = search[row + i][col + j]
    except IndexError:
        check = None
    if position == len(word):
        return True
    if (row + i >= 0 and col + j >= 0) and check == word[position]:
        j += 1 if j > 0 else -1 if j < 0 else 0
        i += 1 if i > 0 else -1 if i < 0 else 0
        position += 1
        return check_line(search, row, col, i, j, word, position)
    else:
        return False


def main() -> None:
    search = get_input("./input.txt")
    check_search(search)


if __name__ == "__main__":
    main()
