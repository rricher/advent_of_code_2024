def main() -> None:
    safe = 0
    data = []
    with open("./failing.txt", "r") as file:
        for line in file:
            numbers = []
            for item in line.split():
                numbers.append(int(item))
            data.append(numbers)
    # print(data[0])
    # for i in range(len(data[0])):
    #     level = [obj for j, obj in enumerate(data[0]) if j != i]
    #     print(level)
    for report in data:
        for i in range(len(report)):
            level = [obj for j, obj in enumerate(report) if j != i]
            if check(level):
                safe += 1
                print(report)
                break
    print(safe)


def check(level):
    if level[0] < level[1]:
        inc = True
    else:
        inc = False
    for i in range(len(level) - 1):
        diff = 0
        cur = level[i]
        next = level[i + 1]
        if inc:
            diff = next - cur
        else:
            diff = cur - next
        if diff < 1 or diff > 3:
            return False
    print(level)
    return True


if __name__ == "__main__":
    main()
