def crabs(positions):
    fuels = []
    for move in range(max(positions)):
        # part a
        # fuel = sum([abs(move - x) for x in positions])
        # part b
        fuel = sum([sum(range(abs(move - x) + 1)) for x in positions])
        fuels.append(fuel)
    return min(fuels)


if __name__ == "__main__":
    with open("day07.txt") as file:
        inp = file.readlines()
        ages = inp[0].split(",")
        positions = list(map(int, ages))
        print(crabs(positions))
