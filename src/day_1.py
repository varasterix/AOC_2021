def inputs_handler(input_file):
    inp = []
    with open(input_file) as file:
        for item in file.readlines():
            inp.append(int(item[:-1]))
    return inp


def compute_diff_last(inp_list):
    increased = 0
    for i in range(1, len(inp_list)):
        if inp_list[i] > inp_list[i - 1]:
            increased += 1
        else:
            pass
    print(increased)


def compute_sliding_diff(inp_list):
    increased = 0
    for i in range(1, len(inp_list) - 2):
        sum_current_window = inp_list[i - 1] + inp_list[i] + inp_list[i + 1]
        sum_next_window = inp_list[i] + inp_list[i + 1] + inp_list[i + 2]
        if sum_current_window < sum_next_window:
            increased += 1
        else:
            pass
    print(increased)


if __name__ == "__main__":
    inputs = inputs_handler("inputs/day_1.txt")

    # Part 1
    print("===Part 1===")
    # compute_diff_last([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    compute_diff_last(inputs)

    # Part 2
    print("===Part 2===")
    # compute_sliding_diff([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    compute_sliding_diff(inputs)
