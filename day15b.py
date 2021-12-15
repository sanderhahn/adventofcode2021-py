from queue import PriorityQueue

with open("day15.txt") as f:
    content = f.read()

def parse_map(content):
    risks = [row for row in content.strip().split("\n")]
    return [[int(cell) for cell in row] for row in risks]

def dump_map(risks_map, width, height):
    for y in range(height):
        print("".join([str(get_risk(risks_map, (x, y))) for x in range(width)]))

def determine_neighbors(position, width, height):
    neighbors = []
    (x, y) = position
    if x > 0:
        neighbors.append((x-1, y))
    if x < width - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < height - 1:
        neighbors.append((x, y+1))
    return set(neighbors)

def get_risk(risks_map, position):
    width, height = len(risks_map[0]), len(risks_map)
    (x, y) = position
    dx = int(x / width)
    dy = int(y / height)
    x %= width
    y %= height
    value = (risks_map[y][x] + dx + dy - 1) % 9
    return value + 1

def process(content):
    risks_map = parse_map(content)
    width, height = len(risks_map[0]), len(risks_map)
    width *= 5
    height *= 5
    # dump_map(risks_map, width, height)
    visited = set()
    distance = {}
    for position in [(x, y) for x in range(width) for y in range(height)]:
        distance[position] = float("inf")
    distance[(0, 0)] = 0
    visited.add((0, 0))

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    # https://stackabuse.com/dijkstras-algorithm-in-python/
    while not pq.empty():
        (dist, current) = pq.get()
        # print(current, dist)
        visited.add(current)
        for neighbor in determine_neighbors(current, width, height):
            if neighbor not in visited:
                old_distance = distance[neighbor]
                new_distance = get_risk(risks_map, neighbor) + dist
                if new_distance < old_distance:
                    pq.put((new_distance, neighbor))
                    distance[neighbor] = new_distance

    end = (width - 1, height - 1)
    return distance[end]

assert process("""\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""") == 315

assert process(content) == 3002

print(process(content))
