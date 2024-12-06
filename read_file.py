def get_input(file_path: str) -> list:
    input = []
    with open(file_path, "r") as file:
        for line in file:
            input.append(line.strip())
    return input


if __name__ == "__main__":
    get_input()
