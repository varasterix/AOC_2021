def inputs_handler(input_file):
    inp = []
    with open(input_file) as file:
        for item in file.readlines():
            inp.append(item[:-1])
    return inp


def binary_str_to_decimal_int(bin):
    res = 0
    length = len(bin)
    for n in range(length):
        res += int(bin[n]) * (2 ** (length - n - 1))
    return res


def compute_rates(diagnostic):
    bin_gamma = ''
    bin_epsilon =  ''
    length = len(diagnostic[0])
    for digit in range(length):
        count_0 = 0
        count_1 = 0
        for diag in diagnostic:
            if int(diag[digit]) == 1:
                count_1 += 1
            elif int(diag[digit]) == 0:
                count_0 += 1
            else:
                raise ValueError
        if count_0 > count_1:
            bin_gamma += '0'
            bin_epsilon += '1'
        elif count_0 < count_1:
            bin_gamma += '1'
            bin_epsilon += '0'
        else:
            raise ValueError
    gamma = binary_str_to_decimal_int(bin_gamma)
    epsilon = binary_str_to_decimal_int(bin_epsilon)
    return gamma * epsilon


def compute_o2_rating(diagnostic):
    length = len(diagnostic[0])
    kept = diagnostic
    check = len(kept) + 1
    while len(kept) != 1:
        if len(kept) == check:
            print("This is an infinite loop")
            break
        else:
            for digit in range(length):
                if len(kept) == 1:
                    return kept[0]
                else:
                    kept_0 = []
                    kept_1 = []
                    for diag in kept:
                        if int(diag[digit]) == 1:
                            kept_1.append(diag)
                        elif int(diag[digit]) == 0:
                            kept_0.append(diag)
                        else:
                            raise ValueError
                    if len(kept_0) > len(kept_1):
                        kept = kept_0
                    else:
                        kept = kept_1
                check = len(kept)
    return kept[0]


def compute_co2_rating(diagnostic):
    length = len(diagnostic[0])
    kept = diagnostic
    check = len(kept) + 1
    while len(kept) != 1:
        if len(kept) == check:
            print("This is an infinite loop...")
            break
        else:
            for digit in range(length):
                if len(kept) == 1:
                    return kept[0]
                else:
                    kept_0 = []
                    kept_1 = []
                    for diag in kept:
                        if int(diag[digit]) == 1:
                            kept_1.append(diag)
                        elif int(diag[digit]) == 0:
                            kept_0.append(diag)
                        else:
                            raise ValueError
                    if len(kept_0) > len(kept_1):
                        kept = kept_1
                    else:
                        kept = kept_0
                check = len(kept)
    return kept[0]


def compute_life_support_rating(diagnostic):
    o2 = binary_str_to_decimal_int(compute_o2_rating(diagnostic))
    co2 = binary_str_to_decimal_int(compute_co2_rating(diagnostic))
    return o2 * co2


if __name__ == "__main__":
    inputs = inputs_handler("inputs/day_3.txt")

    # Part 1
    print("===Part 1===")
    print(compute_rates(inputs))

    # Part 2
    print("===Part 2===")
    print(compute_life_support_rating(inputs))

