from read_file import get_input

ms = {"M", "S"}


def check_search(search):
    found = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            if search[i][j] in ms:
                if check_axis(search, i, j):
                    found += 1
    print(found)


def check_axis(search, i, j):
    letter = search[i][j]
    try:
        a = search[i + 1][j + 1]
        opposite = search[i + 2][j + 2]
        flip = search[i + 2][j]
        flip_opposite = search[i][j + 2]
    except IndexError:
        a = None
        opposite = None
        flip = None
        flip_opposite = None
    if a == "A":
        if opposite is not letter and opposite in ms:
            if flip in ms and flip_opposite in ms:
                if flip is not flip_opposite:
                    return True


def main() -> None:
    search = get_input("./input.txt")
    check_search(search)


if __name__ == "__main__":
    main()
