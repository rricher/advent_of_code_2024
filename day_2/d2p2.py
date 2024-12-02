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
        prnt = False
        unsafe = False
        increase = False
        bad = False
        prev = 0
        level = 1
        if (
            (report[0] < report[1] and report[1] < report[2])
            or (report[1] < report[2] and report[2] < report[3])
            or (report[0] < report[2] and report[2] < report[3])
            or (report[0] < report[1] and report[1] < report[3])
        ):
            increase = True
        while level < len(report):
            diff = 0
            if increase:
                diff = report[level] - report[prev]
            else:
                diff = report[prev] - report[level]
            if diff < 1 or diff > 3:
                if bad:
                    # print("increase" if increase else "decrease")
                    if prnt:
                        print(report)
                        print("unsafe", report[prev], report[level])
                    unsafe = True
                    break
                # print(
                #     "increase" if increase else "decrease",
                #     (report[prev], report[level]),
                #     report,
                # )
                # print((report[prev], report[level]))
                # print(report)
                bad = True
                if prev == 0:
                    if increase:
                        diff = report[level + 1] - report[level]
                    else:
                        diff = report[level] - report[level + 1]
                if level + 1 == len(report) - 1:
                    print("end one", report)
                    prnt = True
            else:
                prev = level
            level += 1

        #         if prev == 0:
        #         if increase:
        #             diff = report[level + 1] - report[level]
        #         else:
        #             diff = report[level] - report[level + 1]
        #     if diff > 0 and diff < 4:
        #         report.pop(prev)
        #     else:
        #         report.pop(level)
        #     prev = 0
        #     level = 1
        # else:
        #     prev = level
        #     level += 1

        if not unsafe:
            safe += 1
            if prnt:
                print("safe")
    print(safe)


if __name__ == "__main__":
    main()
