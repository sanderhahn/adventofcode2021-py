from collections import Counter

with open("day07.txt") as f:
    lines = f.readlines()

# https://nl.wikipedia.org/wiki/Somformule_van_Gauss
def fuel_cost_target(depth, target_depth):
    iterations = abs(depth - target_depth)
    return int((iterations * (iterations + 1)) / 2)

assert fuel_cost_target(16, 5) == 66

def fuel_cost(depths, target_depth):
    fuel = 0
    for depth in depths:
        fuel += fuel_cost_target(depth, target_depth)
    return fuel

def process(lines):
    depths = [int(depth) for depth in lines[0].split(",")]
    (min_depth, max_depth) = (min(depths), max(depths))
    fuel = float('inf')
    for depth in range(min_depth, max_depth+1):
        fuel = min(fuel, fuel_cost(depths, depth))
    return fuel

assert process("""16,1,2,0,4,2,7,1,2,14
""".splitlines()) == 168

assert process(lines) == 95519693

print(process(lines))
