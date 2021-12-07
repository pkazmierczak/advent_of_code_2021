from collections import Counter


def fish(ages, days):
    if days == 0:
        return ages

    new_ages = Counter()
    for i in range(8):
        new_ages[i] = ages[i + 1]

    new_ages[6] += ages[0]
    new_ages[8] = ages[0]

    days -= 1

    return fish(new_ages, days)


if __name__ == "__main__":
    with open("day06.txt") as file:
        inp = file.readlines()
        ages = inp[0].split(",")
        ages_int = list(map(int, ages))
        ages_hashed = Counter(ages_int)
        print(fish(ages_hashed, 80).total())
        print(fish(ages_hashed, 256).total())
