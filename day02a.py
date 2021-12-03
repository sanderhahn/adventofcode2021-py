with open("day02.txt") as f:
    lines = f.readlines()

def process(lines):
    (horizontal, vertical) = [0, 0]
    for line in lines:
        (command, value) = line.split()
        value = int(value)
        match command:
            case "forward":
                horizontal += value
            case "up":
                vertical -= value
            case "down":
                vertical += value
    return horizontal * vertical

assert process("""forward 5
down 5
forward 8
up 3
down 8
forward 2
""".splitlines()) == 150

print(process(lines))
