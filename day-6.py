data = open("input/day6.txt").read()


def marker(n):
    for i in range(n, len(data) + 1):
        if len(set(data[i - n : i])) == n:
            return i


print(f"Solution to part 1: {marker(n=4)}")
print(f"Solution to part 2: {marker(n=14)}")
