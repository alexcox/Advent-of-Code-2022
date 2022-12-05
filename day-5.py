from collections import defaultdict

input_stacks, input_moves = open("input/day5.txt").read().split("\n\n")


def parse_stacks(input):
    stacks = defaultdict(list)
    for stack in input.split("\n")[-2::-1]:
        for i in range(0, len(stack), 4):
            if stack[i + 1].isalpha():
                stacks[(i // 4) + 1].append(stack[i + 1])
    return stacks


def move_stacks(input, stacks, keep_order=False):
    for move in input.split("\n"):
        move = move.split()
        stacks[int(move[-1])] += stacks[int(move[-3])][-int(move[1]) :][
            :: 1 if keep_order else -1
        ]
        del stacks[int(move[-3])][-int(move[1]) :]
    return "".join([v[-1] for k, v in stacks.items()])


print(f"Solution to part 1: {move_stacks(input_moves, parse_stacks(input_stacks))}")
print(
    f"Solution to part 1: {move_stacks(input_moves, parse_stacks(input_stacks), True)}"
)
