with open("day03.txt") as f:
    lines = f.readlines()

def filter(lines, position, value):
    return [line for line in lines if line[position] == value]

def oxygen(lines, position):
    bit = [line[position] for line in lines]
    if bit.count("1") >= bit.count("0"):
        lines = filter(lines, position, "1")
    else:
        lines = filter(lines, position, "0")
    if len(lines) == 1:
        return lines[0]
    else:
        return oxygen(lines, position+1)

def co2_scrubber(lines, position):
    bit = [line[position] for line in lines]
    if bit.count("1") >= bit.count("0"):
        lines = filter(lines, position, "0")
    else:
        lines = filter(lines, position, "1")
    if len(lines) == 1:
        return lines[0]
    else:
        return co2_scrubber(lines, position+1)

def process(lines):
    (oxygen_val, co2_scrubber_val) = (oxygen(lines, 0), co2_scrubber(lines, 0))
    (oxygen_val, co2_scrubber_val) = (int(''.join(oxygen_val), 2), int(''.join(co2_scrubber_val), 2))
    return oxygen_val * co2_scrubber_val

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
""".splitlines()) == 230

assert process(lines) == 3277956

print(process(lines))
