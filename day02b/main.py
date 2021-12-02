def calculate_coordinates(lines):
    aim, depth, horizontal = 0, 0, 0
    for line in lines:
        direction, distance = line.split(" ")
        match direction:
            case "down":
                aim += int(distance)
            case "up":
                aim -= int(distance)
            case "forward":
                horizontal += int(distance)
                depth += aim * int(distance)
    return horizontal, depth


if __name__ == "__main__":
    with open("../day02.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        horizontal, depth = calculate_coordinates(lines)
        print(horizontal * depth)
