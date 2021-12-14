with open("day14.txt") as f:
    content = f.read()

def increment_pair(pairs, pair, count):
    if pair in pairs:
        pairs[pair] += count
    else:
        pairs[pair] = count
    return pairs

def perform_step(pairs, rules):
    new_pairs = {}
    for (pair, count) in pairs.items():
        if pair in rules:
            new_pairs = increment_pair(new_pairs, pair[0] + rules[pair], count)
            new_pairs = increment_pair(new_pairs, rules[pair] + pair[1], count)
        else:
            new_pairs = increment_pair(new_pairs, pair, count)
    return new_pairs

def process(content):
    template, rules = content.strip().split("\n\n")
    template += " "
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    pairs = {pair: pairs.count(pair) for pair in pairs}
    rules = [rule.split(" -> ") for rule in rules.split("\n")]
    rules = {k: v for [k, v] in rules}
    for step in range(40):
        pairs = perform_step(pairs, rules)
    counts = {}
    for (pair, count) in pairs.items():
        if pair[0] in counts:
            counts[pair[0]] += count
        else:
            counts[pair[0]] = count
    counts = [(count, letter) for (letter, count) in counts.items()]
    counts = sorted(counts)
    return counts[-1][0] - counts[0][0]

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
""") == 2188189693529

assert process(content) == 2265039461737

print(process(content))
