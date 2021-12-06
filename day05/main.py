class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __repr__(self):
        return f"{self.begin} ----> {self.end}"


def parse_input(input):
    lines = []
    for i in input:
        parsed = i.split("->")
        begin = parsed[0].split(",")
        end = parsed[1].split(",")
        x = Point(int(begin[0]), int(begin[1]))
        y = Point(int(end[0]), int(end[1]))
        lines.append(Line(x, y))
    return lines


# part 1


def dangerous_spots(lines):
    points = {}

    def mark(p):
        if p not in points:
            points[p] = 1
        else:
            points[p] += 1

    for line in lines:
        if line.begin.x == line.end.x:
            # vertical line
            for y in range(
                min(line.begin.y, line.end.y), max(line.begin.y, line.end.y) + 1
            ):
                mark(Point(line.begin.x, y))
        if line.begin.y == line.end.y:
            # horizontal line
            for x in range(
                min(line.begin.x, line.end.x), max(line.begin.x, line.end.x) + 1
            ):
                mark(Point(x, line.begin.y))
    return [p for p in points if points[p] > 1]


# part 2


def dangerous_spots2(lines):
    points = {}

    def mark(p):
        if p not in points:
            points[p] = 1
        else:
            points[p] += 1

    for line in lines:
        if line.begin.x == line.begin.y and line.end.x == line.end.y:
            # diagonal line
            for x in range(
                min(line.begin.x, line.end.x), max(line.begin.y, line.end.y) + 1
            ):
                mark(Point(x, x))
        elif line.begin.x == line.end.x:
            # vertical line
            for y in range(
                min(line.begin.y, line.end.y), max(line.begin.y, line.end.y) + 1
            ):
                mark(Point(line.begin.x, y))
        elif line.begin.y == line.end.y:
            # horizontal line
            for x in range(
                min(line.begin.x, line.end.x), max(line.begin.x, line.end.x) + 1
            ):
                mark(Point(x, line.begin.y))
        else:
            # damn those diagonals
            for x, y in zip(
                range(line.begin.x, line.end.x - 1, -1),
                range(line.begin.y, line.end.y - 1, -1),
            ):
                mark(Point(x, y))
            for x, y in zip(
                range(line.begin.x, line.end.x + 1),
                range(line.begin.y, line.end.y - 1, -1),
            ):
                mark(Point(x, y))
            for x, y in zip(
                range(line.begin.x, line.end.x - 1, -1),
                range(line.begin.y, line.end.y + 1),
            ):
                mark(Point(x, y))
            for x, y in zip(
                range(line.begin.x, line.end.x + 1),
                range(line.begin.y, line.end.y + 1),
            ):
                mark(Point(x, y))
    return [p for p in points if points[p] > 1]


if __name__ == "__main__":
    with open("test.txt") as file:
        inp = file.readlines()
        inp = [line.strip() for line in inp]
        lines = parse_input(inp)
        # points = dangerous_spots(lines)
        points = dangerous_spots2(lines)
        print(len(points))
