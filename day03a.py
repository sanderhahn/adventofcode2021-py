with open("day03.txt") as f:
    lines = f.readlines()

def process(lines):
    bits = [[line[index] for line in lines] for index in range(len(lines[0]))]
    (gamma, epsilon) = ("", "")
    for bit in bits:
        if bit.count("1") > 0:
            if bit.count("1") > bit.count("0"):
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
    (gamma, epsilon) = (int(''.join(gamma), 2), int(''.join(epsilon), 2))
    return gamma * epsilon

assert process("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".splitlines()) == 198

assert process(lines) == 2498354

print(process(lines))
