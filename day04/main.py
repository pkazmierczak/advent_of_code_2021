def parse_input(lines):
    """
    Parses the input and returns an array of draws and an array of boards.

    Boards are dictionaries where key is the index of the board, and the value
    is an array of arrays of rows.
    """
    drawn = lines[0].split(",")

    boards = []
    board = []
    for line in lines[2:]:
        if line != "":
            l = line.split()
            ll = [[x, False] for x in l]  # mark every number as unselected
            board.append(ll)
        else:
            boards.append(board)
            board = []
            continue

    return drawn, boards


# part 1


def bingo(drawn, boards):
    # hi for loop cascade
    for d in drawn:
        for b in boards:
            columns = [[b[i][j] for i in range(len(b))] for j in range(len(b))]
            for r in b:
                for number in r:
                    if number[0] == d:
                        number[1] = True
                    c = columns[r.index(number)]
                    if all(x[1] for x in r) or all(x[1] for x in c):
                        all_numbers_on_board = [number for row in b for number in row]
                        sum_of_all_unmarked = sum(
                            [
                                int(number[0])
                                for number in all_numbers_on_board
                                if not number[1]
                            ]
                        )
                        return sum_of_all_unmarked * int(number[0])


# part 2


def bingo2(drawn, boards):
    # hi for loop cascade
    boards_that_won = []
    for d in drawn:
        for idx, b in enumerate(boards):
            columns = [[b[i][j] for i in range(len(b))] for j in range(len(b))]
            for r in b:
                for number in r:
                    if number[0] == d:
                        number[1] = True
                    c = columns[r.index(number)]
                    if all(x[1] for x in r) or all(x[1] for x in c):
                        all_numbers_on_board = [number for row in b for number in row]
                        sum_of_all_unmarked = sum(
                            [
                                int(number[0])
                                for number in all_numbers_on_board
                                if not number[1]
                            ]
                        )
                        print(
                            f"win on board {idx+1}, score: {sum_of_all_unmarked * int(number[0])}"
                        )
                        boards_that_won.append(idx)
                        if len(set(boards_that_won)) == len(boards):
                            return


if __name__ == "__main__":
    with open("day04.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        drawn, boards = parse_input(lines)
        # print(bingo(drawn, boards))
        bingo2(drawn, boards)
