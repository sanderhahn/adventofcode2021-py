with open("day10.txt") as f:
    lines = f.readlines()

def other_paren(paren):
    match paren:
        case "(":
            return ")"
        case "[":
            return "]"
        case "{":
            return "}"
        case "<":
            return ">"
    return None

def process_line(line):
    stack = []
    for paren in line.strip():
        other = other_paren(paren)
        if other != None:
            stack.append(other)
        else:
            if len(stack) > 0 and stack[-1] == paren:
                stack.pop()
            elif paren == ")":
                return 3
            elif paren == "]":
                return 57
            elif paren == "}":
                return 1197
            elif paren == ">":
                return 25137
    return 0

def process(lines):
    score = 0
    for line in lines:
        score += process_line(line)
    return score

assert process("""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".splitlines()) == 26397

assert process(lines) == 321237

print(process(lines))
