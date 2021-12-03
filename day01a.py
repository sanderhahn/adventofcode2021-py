import math

with open("day01.txt") as f:
    lines = f.readlines()

def process(lines: list[str]) -> int:
    previous = math.inf
    increased = 0
    for line in lines:
        value = int(line)
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
""".splitlines()) == 7

assert process(lines) == 1448

print(process(lines))

