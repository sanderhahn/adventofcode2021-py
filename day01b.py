import math
from typing import Generator

with open("day01.txt") as f:
    lines = f.readlines()

def sliding_window(lines: list[str]) -> Generator[int, None, None]:
    value = []
    for line in lines:
        value.append(int(line))
        if len(value) == 3:
            yield sum(value)
            value.pop(0)

def process(lines: list[str]) -> int:
    previous = math.inf
    increased = 0
    for value in sliding_window(lines):
        if value > previous:
            increased += 1
        previous = value
    return increased

assert process("""199
200
208
210
200
207
240
269
260
263
""".splitlines()) == 5

assert process(lines) == 1471

print(process(lines))
