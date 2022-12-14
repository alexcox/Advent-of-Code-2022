from itertools import zip_longest

data = list(map(str.splitlines, open("input/day13.txt").read().split("\n\n")))
packet_pairs = [[eval(s) for s in packet] for packet in data]
packets = [eval(s) for packet in data for s in packet]


def compare(left, right):
    queue = [(left, right)]
    while queue:
        left, right = queue.pop()
        if right is None:
            return False
        elif left is None:
            return True
        elif type(left) == type(right) == int:
            if left < right:
                break
            elif left > right:
                return False
        elif type(left) == type(right) == list:
            if (len(left) == 0) ^ (len(right) == 0):
                return len(left) == 0
            queue.extend(list(zip_longest(left, right))[::-1])
        else:
            queue.append(
                (
                    left if type(left) == list else [left],
                    right if type(right) == list else [right],
                )
            )
    return True


def part1():
    return sum(
        [
            i + 1 if compare(left, right) else 0
            for i, (left, right) in enumerate(packet_pairs)
        ]
    )


def insertion_sort(array, compare_function):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and compare_function(
            array[currentPosition - 1], currentValue
        ):
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue
    return array


def part2():
    p = insertion_sort([[[2]], [[6]]] + packets, compare)[::-1]
    return (p.index([[2]]) + 1) * (p.index([[6]]) + 1)


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
