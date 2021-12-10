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
                return []
            elif paren == "]":
                return []
            elif paren == "}":
                return []
            elif paren == ">":
                return []
    return stack

def process(lines):
    scores = []
    for line in lines:
        complete = process_line(line)
        score = 0
        for append in reversed(complete):
            score *= 5
            match append:
                case ")":
                    score += 1
                case "]":
                    score += 2
                case "}":
                    score += 3
                case ">":
                    score += 4
        if score > 0:
            scores.append(score)
    scores = sorted(scores)
    return scores[round(len(scores) / 2)]

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
""".splitlines()) == 288957

assert process(lines) == 2360030859

print(process(lines))
