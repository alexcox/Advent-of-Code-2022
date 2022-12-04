import re

data = [
    [set(range(int(x[0]), int(x[1]) + 1)), set(range(int(x[2]), int(x[3]) + 1))]
    for x in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", open("input/day4.txt").read())
]

part1 = sum([1 if x.issubset(y) or y.issubset(x) else 0 for x, y in data])
part2 = sum([1 if len(x.intersection(y)) > 0 else 0 for x, y in data])

print(f"Solution to part 1: {part1}")
print(f"Solution to part 2: {part2}")
