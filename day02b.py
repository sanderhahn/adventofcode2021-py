with open("day02.txt") as f:
    lines = f.readlines()

def process(lines):
    (horizontal, vertical, aim) = [0, 0, 0]
    for line in lines:
        (command, value) = line.split()
        value = int(value)
        match command:
            case "forward":
                horizontal += value
                vertical += aim * value
            case "up":
                aim -= value
            case "down":
                aim += value
    return horizontal * vertical

assert process("""forward 5
down 5
forward 8
up 3
down 8
forward 2
""".splitlines()) == 900

print(process(lines))
