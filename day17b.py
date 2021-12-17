with open("day17.txt") as f:
    content = f.read()

def debug(val):
    print(val)
    return val

def hit_target(probe, target_area):
    return probe[0] >= target_area[0][0] and \
        probe[0] <= target_area[0][1] and \
        probe[1] >= target_area[1][0] and \
        probe[1] <= target_area[1][1]

assert hit_target([0, 0], [[0, 1], [0, 1]])
assert not hit_target([0, 0], [[1, 1], [1, 1]])

def out_of_reach(probe, velocity, target_area):
    if velocity[0] == 0:
        return probe[1] < min(target_area[1])
    return probe[0] > max(target_area[0])

def probe_step(probe, velocity):
    probe[0] += velocity[0]
    probe[1] += velocity[1]
    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1
    velocity[1] -= 1
    return (probe, velocity)

def simulate(velocity, target_area):
    probe = [0, 0]
    while True:
        (probe, velocity) = probe_step(probe, velocity)
        if hit_target(probe, target_area):
            return True
        if out_of_reach(probe, velocity, target_area):
            return False

assert simulate([7, 2], [[20, 30], [-10, -5]])
assert simulate([6, 3], [[20, 30], [-10, -5]])
assert simulate([9, 0], [[20, 30], [-10, -5]])
assert not simulate([17, -4], [[20, 30], [-10, -5]])

def process(input):
    target_area = [part[2:].split("..") for part in input.removeprefix("target area: ").split(", ")]
    target_area = [[int(c) for c in start_end] for start_end in target_area]

    hits = 0
    for dx in range(100):
        for dy in range(1000, -1000, -1):
            if simulate([dx, dy], target_area):
                hits += 1
    return debug(hits)

assert process("target area: x=20..30, y=-10..-5") == 112

answer = process(content)
assert answer == 4433

print(answer)
