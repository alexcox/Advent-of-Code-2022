input = [[int(x) for x in line] for line in open("input/day8.txt").read().splitlines()]
dim_x, dim_y = len(input), len(input[0])


def cardinal_segments(i, j):
    vertical_slice = [input[k][j] for k in range(dim_x)]
    north = vertical_slice[:i]
    east = input[i][:j:-1]
    south = vertical_slice[:i:-1]
    west = input[i][:j]
    return [north, east, south, west]


def part1():
    n_visible = 0
    for i in range(dim_x):
        for j in range(dim_y):
            tree = input[i][j]
            if (
                i % (dim_x - 1) == 0
                or j % (dim_y - 1) == 0
                or tree > min([max(s) for s in cardinal_segments(i, j)])
            ):
                n_visible += 1
    return n_visible


def part2():
    scores = []
    for i in range(dim_x):
        for j in range(dim_y):
            scores += [1]
            current_tree = input[i][j]
            for segment in cardinal_segments(i, j):
                length = 0
                while len(segment) > 0:
                    length += 1
                    if segment.pop() >= current_tree:
                        break
                scores[-1] *= length
    return max(scores)


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
