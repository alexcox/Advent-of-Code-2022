import copy

data = [
    [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]
    for line in open("input/day14.txt").read().splitlines()
]
source = (500, 0)
grid = {}
for line in data:
    for start, end in zip(line, line[1:]):
        if start[0] == end[0]:
            direction = 1 if end[1] > start[1] else -1
            for i in range(start[1], end[1] + direction, direction):
                grid[(start[0], i)] = True
        else:
            direction = 1 if end[0] > start[0] else -1
            for i in range(start[0], end[0] + direction, direction):
                grid[(i, start[1])] = True
floor_height = max(grid, key=lambda x: x[1])[1]


def part1(grid):
    grid = copy.deepcopy(grid)
    breached_abyss = False
    n_settled = 0
    while not breached_abyss:
        pos = source
        settled = False
        while not settled:
            if pos[1] > floor_height:
                breached_abyss = True
                break
            if (new_pos := (pos[0], pos[1] + 1)) not in grid:
                pos = new_pos
            elif (new_pos := (pos[0] - 1, pos[1] + 1)) not in grid:
                pos = new_pos
            elif (new_pos := (pos[0] + 1, pos[1] + 1)) not in grid:
                pos = new_pos
            else:
                settled = True
        n_settled += 1
        grid[pos] = True
    return n_settled - 1


def part2(grid):
    grid = copy.deepcopy(grid)
    n_settled = 0
    while True:
        pos = source
        settled = False
        while not settled:
            if pos[1] == floor_height + 1:
                settled = True
            elif (new_pos := (pos[0], pos[1] + 1)) not in grid:
                pos = new_pos
            elif (new_pos := (pos[0] - 1, pos[1] + 1)) not in grid:
                pos = new_pos
            elif (new_pos := (pos[0] + 1, pos[1] + 1)) not in grid:
                pos = new_pos
            else:
                settled = True
        n_settled += 1
        if pos == source:
            return n_settled
        grid[pos] = True


print(f"Solution to part 1: {part1(grid)}")
print(f"Solution to part 2: {part2(grid)}")
