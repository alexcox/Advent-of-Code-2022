data = open("input/day10.txt").read().splitlines()
x_register = [1]
for command in data:
    x_register.append(x_register[-1])
    if command.startswith("add"):
        _, increment = command.split()
        x_register.append(x_register[-1] + int(increment))


def part1():
    return sum([i * x_register[i - 1] for i in range(20, len(x_register), 40)])


def part2():
    grid = [
        "#" if i % 40 - 1 <= value <= i % 40 + 1 else "."
        for i, value in enumerate(x_register)
    ]
    return "\n".join(["".join(grid[i * 40 : (i + 1) * 40]) for i in range(6)])


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: \n{part2()}")
