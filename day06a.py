with open("day06.txt") as f:
    content = f.read()

def process(content):
    ages = [int(age) for age in content.strip().split(",")]
    for _ in range(80):
        more_fish = []
        for (i, age) in enumerate(ages):
            if age == 0:
                more_fish.append(8)
                ages[i] = 6
            else:
                ages[i] -= 1
        ages.extend(more_fish)
    return len(ages)

assert process("3,4,3,1,2") == 5934

assert process(content) == 361169

print(process(content))
