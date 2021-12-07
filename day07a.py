from collections import Counter

with open("day07.txt") as f:
    lines = f.readlines()

def fuel_cost(depths, target_depth):
    fuel = 0
    for depth in depths:
        fuel += abs(depth - target_depth)
    return fuel

def process(lines):
    depths = [int(depth) for depth in lines[0].split(",")]
    (min_depth, max_depth) = (min(depths), max(depths))
    fuel = float('inf')
    for depth in range(min_depth, max_depth+1):
        fuel = min(fuel, fuel_cost(depths, depth))
    return fuel

assert process("""16,1,2,0,4,2,7,1,2,14
""".splitlines()) == 37

assert process(lines) == 352707

print(process(lines))
