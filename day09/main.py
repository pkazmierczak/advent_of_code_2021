import numpy as np

# part A, BFS


def low_points(array):
    points = []

    def vertical(point, index, row_num):
        if row_num == 0:
            if point < array[row_num + 1][index]:
                points.append(point)
        elif row_num == len(array) - 1:
            if point < array[row_num - 1][index]:
                points.append(point)
        else:
            if array[row_num + 1][index] > point < array[row_num - 1][index]:
                points.append(point)

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

    return sum(map(lambda x: x + 1, points))


# part B


if __name__ == "__main__":
    with open("test.txt") as file:
        inp = file.readlines()
        array = np.asarray(
            list(map(list, map(lambda x: x.strip("\n"), inp))), dtype=int
        )
        print(low_points(array))
        # print(basins(array))
