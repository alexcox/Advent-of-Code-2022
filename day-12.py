import numpy as np
import heapq

grid = np.array([list(line) for line in open("input/day12.txt").read().splitlines()])

m = len(grid)
n = len(grid[0])


def neighbours(x: int, y: int) -> list[tuple[int, int]]:
    t = [-1, 0, 1]
    return [
        (x + i, y + j)
        for i in t
        for j in t
        if abs(i + j) == 1 and 0 <= x + i < m and 0 <= y + j < n
    ]


def position(char: str) -> tuple[int, int]:
    for i in range(m):
        for j in range(n):
            if grid[i, j] == char:
                return (i, j)


def shortest_path(start: tuple[int, int], target: tuple[int, int]) -> int:
    dist = {(i, j): float("inf") for i in range(m) for j in range(n)}
    dist[start] = 0
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        distance, point = heapq.heappop(queue)
        for neighbour in neighbours(*point):
            alt = distance + 1
            if (
                (point == start and grid[neighbour] == "a")
                or (neighbour == target and grid[point] == "z")
                or 97 <= ord(grid[neighbour]) <= ord(grid[point]) + 1
            ):
                if alt < dist[neighbour]:
                    heapq.heappush(queue, (alt, neighbour))
                    dist[neighbour] = alt
    return dist[target]


def part1() -> int:
    start = position("S")
    target = position("E")
    return shortest_path(start, target)


def part2() -> int:
    target = position("E")
    return min(
        [
            shortest_path(start=(i, j), target=target)
            for i in range(m)
            for j in range(n)
            if grid[i, j] in ["S", "a"]
        ]
    )


print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
