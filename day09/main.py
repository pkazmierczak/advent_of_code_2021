from collections import namedtuple

import numpy as np

Point = namedtuple("Point", ["value", "index", "row_num"])

# part A


def low_points(array):
    points = []

    def vertical(point, index, row_num):
        if row_num == 0:
            if point < array[row_num + 1][index]:
                points.append(Point(point, index, row_num))
        elif row_num == len(array) - 1:
            if point < array[row_num - 1][index]:
                points.append(Point(point, index, row_num))
        else:
            if array[row_num + 1][index] > point < array[row_num - 1][index]:
                points.append(Point(point, index, row_num))

    for row_num, row in enumerate(array):
        for i in range(len(row)):
            if i == 0:
                if row[i] < row[i + 1]:
                    vertical(row[i], i, row_num)
            elif i == len(row) - 1:
                if row[i] < row[i - 1]:
                    vertical(row[i], i, row_num)
            else:
                if row[i - 1] > row[i] < row[i + 1]:
                    vertical(row[i], i, row_num)

    return points


# part B


def basins(array):
    basin_sizes = []

    l_points = low_points(array)
    # for point in l_points:

    print(basin_sizes)
    return np.prod(np.array(basin_sizes))


if __name__ == "__main__":
    with open("test.txt") as file:
        inp = file.readlines()
        array = np.asarray(
            list(map(list, map(lambda x: x.strip("\n"), inp))), dtype=int
        )
        # print(low_points(array))
        print(basins(array))
