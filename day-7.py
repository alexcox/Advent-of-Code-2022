from collections import defaultdict

commands = [
    x.strip("\n").split("\n") for x in open("input/day7.txt").read().split("$ ")[1:]
]

path = []
files = defaultdict(list)

for batch in commands:
    command, *args = batch[0].split()
    if command == "cd":
        if args[0] == "/":
            path = [""]
        elif args[0] == "..":
            path.pop()
        else:
            path.append(args[0])
    elif command == "ls":
        for file in batch[1:]:
            x, y = file.split()
            if x != "dir":
                for i in range(len(path)):
                    files["/".join(path[: i + 1])].append(int(x))


def part1():
    return sum([sum(v) for k, v in files.items() if sum(v) <= 100_000])


def part2():
    delta = {
        k: sum(v) - sum(files[""]) - 40_000_000
        for k, v in files.items()
        if sum(v) >= sum(files[""]) - 40_000_000
    }
    return sum(files[min(delta, key=delta.get)])


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
