win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}

data = list(map(lambda x: x.split(), open("input/day2.txt").read().splitlines()))


def calculate(values):
    return sum(
        [
            ord(y) - 87 + (6 if win[x] == y else 3 if draw[x] == y else 0)
            for x, y in values
        ]
    )


def pre_process(values):
    return [
        [x, lose[x] if y == "X" else draw[x] if y == "Y" else win[x]] for x, y in values
    ]


print(f"Answer to part 1: {calculate(data)}")
print(f"Answer to part 2: {calculate(pre_process(data))}")
