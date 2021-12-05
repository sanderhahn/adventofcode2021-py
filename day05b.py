import re

with open("day05.txt") as f:
    content = f.readlines()

def increment_map(map, position):
    if not position in map:
        map[position] = 1
    else:
        map[position] += 1

def process(lines):
    map = {}
    for line in lines:
        (start, end) = line.split(" -> ")
        (start_x, start_y) = start.split(",")
        (end_x, end_y) = end.split(",")
        (start_x, start_y) = (int(start_x), int(start_y))
        (end_x, end_y) = (int(end_x), int(end_y))
        if start_x == end_x:
            if end_y < start_y:
                (start_y, end_y) = (end_y, start_y)
            for y in range(start_y, end_y+1):
                increment_map(map, (start_x, y))
        elif start_y == end_y:
            if end_x < start_x:
                (start_x, end_x) = (end_x, start_x)
            for x in range(start_x, end_x+1):
                increment_map(map, (x, start_y))
        else:
            x = start_x
            y = start_y
            if end_x < start_x:
                iterations = start_x - end_x
            else:
                iterations = end_x - start_x
            for _ in range(iterations + 1):
                increment_map(map, (x, y))
                if end_x > start_x:
                    x += 1
                elif start_x > end_x:
                    x -= 1
                if end_y > start_y:
                    y += 1
                elif start_y > end_y:
                    y -= 1
    dangerous = 0
    for value in map.values():
        if value >= 2:
            dangerous += 1
    return dangerous

assert process("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".splitlines()) == 12

assert process(content) == 23864

print(process(content))
