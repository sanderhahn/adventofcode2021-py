from functools import reduce

with open("day09.txt") as f:
    lines = f.readlines()

def read_map(lines):
    return [[int(height) for height in line.strip()] for line in lines]

def adjacent(map, x, y):
    adjacent = []
    if x > 0:
        adjacent.append(map[y][x-1])
    if x < len(map[0]) - 1:
        adjacent.append(map[y][x+1])
    if y > 0:
        adjacent.append(map[y-1][x])
    if y < len(map) - 1:
        adjacent.append(map[y+1][x])
    return adjacent

def fill_basin(map, basin, x, y):
    if map[y][x] == 9:
        return basin
    elif (x, y) in basin:
        return basin
    else:
        basin.append((x, y))
    if x > 0:
        basin = fill_basin(map, basin, x-1, y)
    if x < len(map[0]) - 1:
        basin = fill_basin(map, basin, x+1, y)
    if y > 0:
        basin = fill_basin(map, basin, x, y-1)
    if y < len(map) - 1:
        basin = fill_basin(map, basin, x, y+1)
    return basin

def process(lines):
    height_map = read_map(lines)
    low_points = []
    for y in range(len(height_map)):
        for x in range(len(height_map[0])):
            height = height_map[y][x]
            neighbor_heights = adjacent(height_map, x, y)
            if all(map(lambda adjacent_height : height < adjacent_height, neighbor_heights)):
                low_points.append((x, y))
    basin_sizes = {(x, y): len(fill_basin(height_map, [], x, y)) for (x, y) in low_points}
    top_3 = list(reversed(sorted(basin_sizes.values())))[:3]
    return reduce(lambda x, y: x * y, top_3)

assert process("""2199943210
3987894921
9856789892
8767896789
9899965678
""".splitlines()) == 1134

assert process(lines) == 902880

print(process(lines))
