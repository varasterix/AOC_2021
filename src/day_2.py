def inputs_handler(input_file):
    inp = []
    with open(input_file) as file:
        for item in file.readlines():
            res = item[:-1].split(' ')
            inp.append([res[0], int(res[1])])
    return inp


def calculate_position_no_aim(course):
    horizontal = 0
    depth = 0
    for item in course:
        if item[0] == "up":
            depth -= item[1]
        elif item[0] == "down":
            depth += item[1]
        elif item[0] == "forward":
            horizontal += item[1]
    return horizontal * depth


def calculate_position_with_aim(course):
    horizontal = 0
    depth = 0
    aim = 0
    for item in course:
        if item[0] == "up":
            aim -= item[1]
        elif item[0] == "down":
            aim += item[1]
        elif item[0] == "forward":
            horizontal += item[1]
            depth += aim * item[1]
    return horizontal * depth


if __name__ == "__main__":
    inputs = inputs_handler("inputs/day_2.txt")

    # Part 1
    print("===Part 1===")
    print(calculate_position_no_aim(inputs))

    # Part 2
    print("===Part 2===")
    print(calculate_position_with_aim(inputs))

