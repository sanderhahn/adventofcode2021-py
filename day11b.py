with open("day11.txt") as f:
    lines = f.readlines()

def parse_map(lines):
    return [[int(char) for char in line.strip()] for line in lines]

def dump_map(map):
    for line in map:
       print("".join([str(octo) for octo in line]))
    print()

def flash(map, x, y, flashed = {}):
    if x < 0 or y < 0 or x > len(map[0]) - 1 or y > len(map) - 1:
        return flashed
    elif (x, y) in flashed:
        return flashed
    map[y][x] += 1
    if map[y][x] > 9:
        flashed[(x, y)] = True
        flashed = flash(map, x-1, y-1, flashed)
        flashed = flash(map, x, y-1, flashed)
        flashed = flash(map, x+1, y-1, flashed)
        flashed = flash(map, x+1, y, flashed)
        flashed = flash(map, x+1, y+1, flashed)
        flashed = flash(map, x, y+1, flashed)
        flashed = flash(map, x-1, y+1, flashed)
        flashed = flash(map, x-1, y, flashed)
    return flashed

def step(map):
    flashed = {}
    for (y, row) in enumerate(map):
        for (x, _) in enumerate(row):
            flashed = flash(map, x, y, flashed)
    for (y, row) in enumerate(map):
        for (x, _) in enumerate(row):
            if map[y][x] > 9:
                map[y][x] = 0
    return len(flashed)

def process(lines):
    map = parse_map(lines)
    i = 0
    while True:
        flashes = step(map)
        i += 1
        if flashes == len(map) * len(map[0]):
            break
        # dump_map(map)
    return i

assert process("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".splitlines()) == 195

assert process(lines) == 418

print(process(lines))
