import json
import math

with open("day18.txt") as f:
    lines = f.readlines()

def debug(val):
    print(val)
    return val

def parse_number(number):
    list = []
    for c in number.strip():
        if c.isnumeric():
            if type(list[-1]) == int:
                list[-1] *= 10
                list[-1] += int(c)
            else:
                list.append(int(c))
        else:
            list.append(c)
    return list

def number_to_string(num):
    return "".join([str(item) for item in num])

def magnitude(number):
    if type(number[0]) == list:
        left = magnitude(number[0])
    else:
        left = number[0]
    if type(number[1]) == list:
        right = magnitude(number[1])
    else:
        right = number[1]
    return 3*left + 2*right

assert magnitude([9,1]) == 29
assert magnitude([[9,1],[1,9]]) == 129
assert magnitude([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]) == 4140

def add(a, b):
    c = ["[", *a, ",", *b, "]"]
    # print("add", number_to_string(c))
    while True:
        (c, exploded) = explode(c)
        if exploded:
            # print("explode", number_to_string(c))
            continue
        (c, splited) = split(c)
        if splited:
            # print("split", number_to_string(c))
            continue
        break
    return c

def process_addition(lines):
    num = parse_number(lines.pop(0))
    for line in lines:
        next = parse_number(line)
        num = add(num, next)
    return number_to_string(num)

def split(list):
    splited = False
    for (i, item) in enumerate(list):
        if type(item) == int and item >= 10:
            list[i:i+1] = ["[", math.floor(item/2) ,",", math.ceil(item/2), "]"]
            splited = True
            break
    return (list, splited)

assert split([0]) == ([0], False)
assert split([10]) == (["[", 5, ",", 5, "]"], True)

def explode(number):
    list = number
    depth = 0
    i = 0
    exploded = False
    while not exploded and i < len(list):
        c = list[i]
        if c == "[":
            depth += 1
        if c == "]":
            depth -= 1
        if depth == 5:
            # print("depth 5 at", list[i:i+5])
            _, left, _, right, *_ = list[i:]
            list[i:i+5] = [0]
            for j in range(i-1, 0, -1):
                if type(list[j]) == int:
                    list[j] += left
                    break
            for j in range(i+1, len(list)):
                if type(list[j]) == int:
                    list[j] += right
                    break
            exploded = True
            break
        i += 1

    return (list, exploded)

assert explode(parse_number("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")) == (parse_number("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"), True)
assert explode(parse_number("[[6,[5,[4,[3,2]]]],1]")) == (parse_number("[[6,[5,[7,0]]],3]"), True)
assert explode(parse_number("[[[[[9,8],1],2],3],4]")) == (parse_number("[[[[0,9],2],3],4]"), True)
assert explode(parse_number("[7,[6,[5,[4,[3,2]]]]]")) == (parse_number("[7,[6,[5,[7,0]]]]"), True)
assert explode(parse_number("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")) == (parse_number("[[3,[2,[8,0]]],[9,[5,[7,0]]]]"), True)

def process(lines):
    max_magnitude = 0
    for x in lines:
        for y in lines:
            total = number_to_string(process_addition([x, y]))
            max_magnitude = max(max_magnitude, magnitude(json.loads(total)))
            total = number_to_string(process_addition([y, x]))
            max_magnitude = max(max_magnitude, magnitude(json.loads(total)))
    return max_magnitude

assert process_addition("""\
[1,1]
[2,2]
[3,3]
[4,4]
""".splitlines()) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"

assert process_addition("""\
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
""".splitlines()) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"

assert process_addition("""\
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
""".splitlines()) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"

assert process_addition("""\
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
""".splitlines()) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

assert process("""\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".splitlines()) == 3993

assert process(lines) == 4747

print(process(lines))
