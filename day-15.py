import re

lines = open("input/day15.txt").read().splitlines()
coords = [[int(d) for d in re.findall(r"=(-?\d+)", line)] for line in lines]


def manhattan_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


sensors = {(a, b): manhattan_distance((a, b), (c, d)) for a, b, c, d in coords}
beacons = {(a, b) for _, _, a, b in coords}


def part1(n_row):
    seen = set()
    for sensor, scan_range in sensors.items():
        y_diff = abs(n_row - sensor[1])
        if y_diff > scan_range:
            continue
        for j in range(
            sensor[0] - scan_range + y_diff, sensor[0] + scan_range - y_diff + 1
        ):
            seen.add((j, n_row))
    return len(seen - beacons)


def boundary(sensor, dist, x, y):
    for j in range(dist + 1):
        if x <= sensor[0] + j <= y:
            if x <= sensor[1] + dist - j + 1 <= y:
                yield (sensor[0] + j, sensor[1] + dist - j + 1)
            if x <= sensor[1] - dist + j - 1 <= y:
                yield (sensor[0] + j, sensor[1] - dist + j - 1)
        if x <= sensor[0] - j <= y:
            if x <= sensor[1] + dist - j + 1 <= y:
                yield (sensor[0] - j, sensor[1] + dist - j + 1)
            if x <= sensor[1] - dist + j - 1 <= y:
                yield (sensor[0] - j, sensor[1] - dist + j - 1)


def part2(x, y):
    for sensor, scan_range in sensors.items():
        for point in boundary(sensor, scan_range, x, y):
            valid = True
            for sensor_b, scan_range_b in sensors.items():
                if not valid:
                    break
                if sensor == sensor_b:
                    continue
                valid &= manhattan_distance(point, sensor_b) > scan_range_b
            if valid:
                return point[0] * 4_000_000 + point[1]


print(f"Solution to part 1: {part1(2_000_000)}")
print(f"Solution to part 2: {part2(0, 4_000_000)}")
