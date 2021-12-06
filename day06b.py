from collections import Counter

with open("day06.txt") as f:
    content = f.read()

def process(content):
    ages = [int(age) for age in content.strip().split(",")]
    by_age = {age: ages.count(age) for age in range(9)}
    for day in range(256):
        new_fish = 0
        reset_fish = 0
        for age in range(9):
            if age == 0:
                reset_fish = by_age[age]
                new_fish = by_age[age]
            else:
                by_age[age-1] = by_age[age]
        by_age[6] += reset_fish
        by_age[8] = new_fish
    return sum(by_age.values())

assert process("3,4,3,1,2") == 26984457539

assert process(content) == 1634946868992

print(process(content))
