from collections import Counter
from math import prod

input_monkeys = [
    monkey.strip().split("\n")
    for monkey in open("input/day11.txt").read().split("\n\n")
]


def monkeys():
    return [
        {
            "items": [int(item_id.rstrip(",")) for item_id in monkey[1].split()[2:]],
            "operation": monkey[2].split("= ")[1],
            "divisible_by": int(monkey[3].split()[-1]),
            "if_true": int(monkey[4].split()[-1]),
            "if_false": int(monkey[5].split()[-1]),
        }
        for monkey in input_monkeys
    ]


monkeys_pt1 = monkeys()
monkeys_pt2 = monkeys()

lcm = prod([monkey["divisible_by"] for monkey in monkeys_pt1] + [3])


def monkey_business(monkeys: list, rounds: int, manage_worry: bool = True):
    inspection_count = Counter()
    for i in range(rounds):
        for idx, monkey in enumerate(monkeys):
            while len(monkey["items"]) > 0:
                inspection_count[idx] += 1
                old = monkey["items"].pop()
                new = eval(monkey["operation"]) % lcm
                if manage_worry:
                    new //= 3
                monkeys[
                    monkey["if_true"]
                    if new % monkey["divisible_by"] == 0
                    else monkey["if_false"]
                ]["items"].append(new)
    return prod([v for k, v in inspection_count.most_common(2)])


print(f"Solution to part 1: {monkey_business(monkeys_pt1, rounds=20)}")
print(
    f"Solution to part 2: {monkey_business(monkeys_pt2, rounds=10000, manage_worry=False)}"
)
