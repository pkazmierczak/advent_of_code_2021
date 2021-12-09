def digits(input):
    counted = 0
    for line in input:
        first_ten, output = map(lambda x: x.split(), line.strip("\n").split("|"))

        # part A
        # for o in output:
        # if len(o) in [2, 4, 3, 7]: # it's either a 1,4,7, or 8
        # counted += 1

        # part B
        s = {  # s
            "t": set(),  # top
            "ul": set(),  # upper left
            "ur": set(),  # upper right
            "m": set(),  # middle
            "ll": set(),  # lower left
            "lr": set(),  # lower right
            "b": set(),  # bottom
        }

        first_ten.sort(key=len)
        for f in first_ten:
            match len(f):
                case 2:  # 1
                    s["ur"] = set([f[0], f[1]])
                    s["lr"] = set([f[0], f[1]])  # we don't know which is which yet
                case 3:  # 7
                    s["t"] = set(
                        [c for c in f if c not in s["ur"] and c not in s["lr"]]
                    )
                case 4:  # 4
                    s["ul"] = set(
                        [c for c in f if c not in s["ur"] and c not in s["lr"]]
                    )
                    s["m"] = s["ul"]
                case 5:
                    five_chars = set(f)
                    if s["ur"].issubset(five_chars):  # 3
                        five_chars.difference_update(s["ur"])
                        five_chars.difference_update(s["t"])
                        s["m"] = five_chars.intersection(s["m"])
                        s["ul"].difference_update(s["m"])
                        s["b"] = five_chars.difference(s["m"])

                case 6:
                    six_chars = set(f)
                    lr = s["ur"].intersection(six_chars).intersection(s["lr"])
                    if len(lr) == 1:  # 6
                        s["lr"] = lr
                        s["ur"].difference_update(lr)

                case 7:  # 8
                    s["ll"] = set(
                        [
                            c
                            for c in f
                            if c
                            not in s["ur"]
                            .union(s["ul"])
                            .union(s["lr"])
                            .union(s["t"])
                            .union(s["m"])
                            .union(s["b"])
                        ]
                    )

        zero = s["t"].union(s["ul"], s["ur"], s["ll"], s["lr"], s["b"])
        one = s["ur"].union(s["lr"])
        two = s["t"].union(s["ur"], s["m"], s["ll"], s["b"])
        three = s["t"].union(s["ur"], s["m"], s["lr"], s["b"])
        four = s["ul"].union(s["ur"], s["m"], s["lr"])
        five = s["t"].union(s["ul"], s["m"], s["lr"], s["b"])
        six = s["t"].union(s["ul"], s["m"], s["ll"], s["lr"], s["b"])
        seven = s["t"].union(s["ur"], s["lr"])
        eight = s["t"].union(s["ul"], s["ur"], s["m"], s["ll"], s["lr"], s["b"])
        nine = s["t"].union(s["ul"], s["ur"], s["m"], s["lr"], s["b"])

        decoded_output = ""
        for o in output:
            if set(o) == zero:
                decoded_output += "0"
            elif set(o) == one:
                decoded_output += "1"
            elif set(o) == two:
                decoded_output += "2"
            elif set(o) == three:
                decoded_output += "3"
            elif set(o) == four:
                decoded_output += "4"
            elif set(o) == five:
                decoded_output += "5"
            elif set(o) == six:
                decoded_output += "6"
            elif set(o) == seven:
                decoded_output += "7"
            elif set(o) == eight:
                decoded_output += "8"
            elif set(o) == nine:
                decoded_output += "9"

        counted += int(decoded_output)

    return counted


if __name__ == "__main__":
    with open("day08.txt") as file:
        inp = file.readlines()
        print(digits(inp))
