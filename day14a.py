from collections import Counter

with open("day14.txt") as f:
    content = f.read()

def perform_step(template, rules):
    new_template = ""
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair in rules:
            new_template += pair[0] + rules[pair]
        else:
            new_template += pair
    new_template += template[-1]
    return new_template

def process(content):
    template, rules = content.strip().split("\n\n")
    rules = [rule.split(" -> ") for rule in rules.split("\n")]
    rules = {k: v for [k, v] in rules}
    for i in range(10):
        template = perform_step(template, rules)
    counts = Counter(template).most_common()
    return counts[0][1] - counts[-1][1]

assert process("""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""") == 1588

assert process(content) == 2027

print(process(content))
