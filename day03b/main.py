def filtered_lines(lst, pos, bit):
    return [x for x in lst if x[pos] == bit]


def _calculate(lines, more_zeroes_filter, less_zeroes_or_equal_filter):
    for i in range(len(lines[0])):
        # create a vertical line for this bit position
        v_line = [line[i] for line in lines]

        # are there more zeroes in that line?
        if v_line.count("0") > v_line.count("1"):
            lines = filtered_lines(lines, i, more_zeroes_filter)
        else:
            lines = filtered_lines(lines, i, less_zeroes_or_equal_filter)

        if len(lines) == 1:
            break

    return int(lines[0], 2)


def calculate_oxygen(lines):
    return _calculate(lines, "0", "1")


def calculate_co2(lines):
    return _calculate(lines, "1", "0")


if __name__ == "__main__":
    with open("../day03.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        print(calculate_oxygen(lines) * calculate_co2(lines))
