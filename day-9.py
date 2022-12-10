directions = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}
instructions = []
for direction, magnitude in map(str.split, open("input/day9.txt").read().splitlines()):
    instructions += [directions[direction]] * int(magnitude)


def add(position, vector):
    return (position[0] + vector[0], position[1] + vector[1])


def adjacent(head, tail):
    return (head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2 <= 2


def compare(x, y, i):
    return 1 if x[i] > y[i] else -1 if x[i] < y[i] else 0


def unique_tail_positions(knots: int):
    head = (0, 0)
    tails = [head] * (knots - 1)
    tail_history = [head]
    for instruction in instructions:
        head = add(head, instruction)
        for i in range(len(tails)):
            rel_head = tails[i - 1] if i > 0 else head
            while not adjacent(rel_head, tails[i]):
                vertical_direction = compare(rel_head, tails[i], 0)
                horizontal_direction = compare(rel_head, tails[i], 1)
                tails[i] = add(tails[i], (vertical_direction, horizontal_direction))
                if i == len(tails) - 1:
                    tail_history.append(tails[i])
    return len(set(tail_history))


print(f"Solution to part 1: {unique_tail_positions(knots=2)}")
print(f"Solution to part 2: {unique_tail_positions(knots=10)}")
