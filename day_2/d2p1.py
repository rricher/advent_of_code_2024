def main() -> None:
    safe = 0
    data = []
    with open("./input.txt", "r") as file:
        for line in file:
            numbers = []
            for item in line.split():
                numbers.append(int(item))
            data.append(numbers)
    for report in data:
        unsafe = False
        increase = False
        prev = 0
        level = 1
        if (
            (report[0] < report[1] and report[1] < report[2])
            or (report[1] < report[2] and report[2] < report[3])
            or (report[0] < report[2] and report[2] < report[3])
            or (report[0] < report[1] and report[1] < report[3])
        ):
            increase = True
        # print(increase, report)
        while level < len(report):
            diff = 0
            if increase:
                diff = report[level] - report[prev]
            else:
                diff = report[prev] - report[level]
            if diff < 1 or diff > 3:
                unsafe = True
                break
            prev = level
            level += 1
        if not unsafe:
            safe += 1
    print(safe)


if __name__ == "__main__":
    main()
