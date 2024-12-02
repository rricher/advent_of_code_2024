def main() -> None:
    safe = 0
    report = []
    with open("./input.txt", "r") as file:
        for line in file:
            numbers = []
            for item in line.split():
                numbers.append(int(item))
            report.append(numbers)

    # for line in report:
    #     unsafe = False
    #     prev = line[0]
    #     inc = None
    #     # bad = False
    #     if line[-1] > prev:
    #         if line[-1] > line[1]:
    #             increasing = True
    #         elif line[1] > line[0] and line[2] < line[1]:
    #             increasing = True
    #     elif line[-1] > line[1]:
    #         if line[-1] > line[2]:
    #             increasing = True
    #         elif line[1] > line[0] and line[2] < line[1]:
    #             increasing = True
    #     for i in range(1, len(line)):
    #         diff = 0
    #         if increasing:
    #             diff = line[i] - prev
    #         else:
    #             diff = prev - line[i]
    #         if diff < 1 or diff > 3:

    for line in report:
        unsafe = False
        increasing = False
        damped = False
        prev = line[0]
        if line[-1] > prev:
            if line[-1] > line[1]:
                increasing = True
            elif line[1] > line[0] and line[2] < line[1]:
                increasing = True
        elif line[-1] > line[1]:
            if line[-1] > line[2]:
                increasing = True
            elif line[1] > line[0] and line[2] < line[1]:
                increasing = True
        for i in range(1, len(line)):
            if increasing:
                if line[i] - prev <= 0 or line[i] - prev >= 4:
                    # print("damped", prev, line[i])
                    if damped:
                        # print("unsafe", prev, line[i], line)
                        # print("increasing")
                        unsafe = True
                        break
                    else:
                        if i == len(line) - 1:
                            # print("damped", prev, line[i])
                            pass
                            # print(line)
                        else:
                            damped = True
                        if i == 1:
                            if prev - line[i + 1] <= 0 or prev - line[i + 1] >= 4:
                                prev = line[i]
                        # elif i + 1 < len(line) - 1:
                        #     if line[i + 1] - prev <= 0 or line[i + 1] - prev >= 4:
                        #         print("increasing", prev, line[i])
                        #         print(line)
                        #         prev = line[i]
                else:
                    prev = line[i]
            else:
                if prev - line[i] <= 0 or prev - line[i] >= 4:
                    # print("damped", prev, line[i])
                    if damped:
                        # print("unsafe", prev, line[i], line)
                        # print("decreasing")
                        unsafe = True
                        break
                    else:
                        if i == len(line) - 1:
                            # print("damped", prev, line[i])
                            pass
                            # print(line)
                        else:
                            damped = True
                        if i == 1:
                            if prev - line[i + 1] <= 0 or prev - line[i + 1] >= 4:
                                prev = line[i]
                        # elif i + 1 < len(line) - 1:
                        #     if prev - line[i + 1] <= 0 or prev - line[i + 1] >= 4:
                        #         print("decreasing", prev, line[i])
                        #         print(line)
                        #         prev = line[i]
                else:
                    prev = line[i]
        if not unsafe:
            if damped:
                print("-----------damped", line)
            safe += 1
    print(safe)


if __name__ == "__main__":
    main()
