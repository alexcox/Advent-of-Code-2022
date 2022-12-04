from functools import reduce

data = open("input/day3.txt").read().splitlines()


def score(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38


def badges(all_elves):
    for i in range(0, len(all_elves), 3):
        yield reduce(
            lambda x, y: x.intersection(y), map(set, all_elves[i : i + 3])
        ).pop()


part1 = sum(
    score(item)
    for backpack in data
    for item in set(backpack[: len(backpack) // 2])
    if item in backpack[len(backpack) // 2 :]
)

part2 = sum(score(badge) for badge in badges(data))

print(f"Solution to part 1: {part1}")
print(f"Solution to part 2: {part2}")
