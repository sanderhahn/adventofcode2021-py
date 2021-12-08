with open("day08.txt") as f:
    lines = f.readlines()

def map_to_digit(digit):
    match len(digit):
        case 2:
            return 1
        case 4:
            return 4
        case 3:
            return 7
        case 7:
            return 8
    return None

def determine_mapping(digits):
    digits = [set(digit) for digit in digits]
    digit_to_segments = {}
    for digit in digits:
        num = map_to_digit(digit)
        if num != None:
            digit_to_segments[num] = digit
    for digit in digits:
        if len(digit) == 5:
            if len(digit_to_segments[1] & digit) == 2:
                num = 3
            elif len(digit_to_segments[4] & digit) == 2:
                num = 2
            else:
                num = 5
        elif len(digit) == 6:
            if len(digit_to_segments[4] & digit) == 4:
                num = 9
            elif len(digit_to_segments[1] & digit) == 1:
                num = 6
            else:
                num = 0
        else:
            continue
        digit_to_segments[num] = digit
    return digit_to_segments

assert determine_mapping("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")) == {8: {'b', 'g', 'a', 'c', 'f', 'd', 'e'}, 7: {'b', 'd', 'a'}, 4: {'f', 'a', 'b', 'e'}, 1: {'b', 'a'}, 5: {'b', 'c', 'f', 'd', 'e'}, 2: {'g', 'a', 'c', 'd', 'f'}, 3: {'b', 'a', 'c', 'd', 'f'}, 9: {'e', 'b', 'a', 'c', 'd', 'f'}, 6: {'b', 'g', 'c', 'f', 'd', 'e'}, 0: {'b', 'g', 'a', 'c', 'd', 'e'}}

def process(lines):
    total = 0
    for line in lines:
        input, output = line.strip().split(" | ")
        input, output = input.split(" "), output.split(" ")
        mapping = determine_mapping(input)
        num = 0
        for digit in output:
            for k, v in mapping.items():
                if set(digit) == v:
                    num *= 10
                    num += k
        total += num
    return total

assert process("""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".splitlines()) == 61229

assert process(lines) == 1091609

print(process(lines))
