import sys

sys.path.insert(0, "C:/Users/ryan/Projects/advent_of_code")

from read_file import get_input

start = ()
x_obs = {}
y_obs = {}
orientation = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}


def get_rotation(facing):
    if facing == "up":
        return "right"
    elif facing == "right":
        return "down"
    elif facing == "down":
        return "left"
    else:
        return "up"


def process_input(input: list[str]):
    floor = []
    for y in range(len(input)):
        string = input[y]
        floor.append([])
        for x in range(len(string)):
            char = string[x]
            if char == "^":
                start = (x, y)
            elif char == "#":
                if x not in x_obs:
                    x_obs[x] = []
                if y not in y_obs:
                    y_obs[y] = []
                x_obs[x].append(y)
                y_obs[y].append(x)
            floor[y].append(char)
    return floor


def check_map(floor):
    # go through whole route checking
    pass


# if right has obstacle,
# then if right has obstacle,
# then if right has obsticle,
# then if in-line with start of check
# you have found loop


def check_loop(floor, current, facing):
    cur_x = current[0]
    cur_y = current[1]
    if facing == "right" or facing == "left":
        if cur_x in x_obs:
            # . . .
            pass
        pass
    else:
        if cur_y in y_obs:
            pass
        pass
    ### Not actual just pseudo
    # for i in range(3):
    #     contin = False
    #     for i in range(len(map[facing]) - start(facing)):
    #         if map[i] == "#":
    #             contin = True
    #             break
    #     if not contin:
    #         return False
    # return True


def main() -> None:
    input = get_input("./test_input.txt")
    floor = process_input(input)
    check_map(floor)


if __name__ == "__main__":
    main()
