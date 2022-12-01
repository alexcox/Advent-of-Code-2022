summed_calories = [
    sum(map(int, calories.split("\n")))
    for calories in open("input/day1.txt").read().split("\n\n")
]
print(f"Answer to part 1: {max(summed_calories)}")
print(f"Answer to part 2: {sum(sorted(summed_calories)[-3:])}")
