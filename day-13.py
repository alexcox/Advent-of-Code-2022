from itertools import zip_longest
from functools import cmp_to_key

data = list(map(str.splitlines, open("input/day13.txt").read().split("\n\n")))
packet_pairs = [[eval(s) for s in packet] for packet in data]
packets = [eval(s) for packet in data for s in packet]


def compare(left, right):
    queue = [(left, right)]
    while queue:
        left, right = queue.pop()
        if right is None:
            return -1
        elif left is None:
            return 1
        elif type(left) == type(right) == int:
            if left < right:
                break
            elif left > right:
                return -1
        elif type(left) == type(right) == list:
            if (len(left) == 0) ^ (len(right) == 0):
                return 1 if len(left) == 0 else -1
            queue.extend(list(zip_longest(left, right))[::-1])
        else:
            queue.append(
                (
                    left if type(left) == list else [left],
                    right if type(right) == list else [right],
                )
            )
    return 1


def part1():
    return sum(
        [
            i + 1 if compare(left, right) == 1 else 0
            for i, (left, right) in enumerate(packet_pairs)
        ]
    )


def part2():
    p = sorted([[[2]], [[6]]] + packets, key=cmp_to_key(compare), reverse=True)
    return (p.index([[2]]) + 1) * (p.index([[6]]) + 1)


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
