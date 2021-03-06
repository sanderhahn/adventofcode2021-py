with open("day13.txt") as f:
    content = f.read()

def flip(coordinate, position):
    coordinate -= position
    coordinate = -coordinate
    coordinate += position
    return coordinate

assert flip(4, 2) == 0

def perform_fold(dots, side, position):
    new_dots = {}
    for (x, y) in dots.keys():
        if side == "y":
            if y > position:
                new_dots[(x, flip(y, position))] = True
            else:
                new_dots[(x, y)] = True
        if side == "x":
            if x > position:
                new_dots[(flip(x, position), y)] = True
            else:
                new_dots[(x, y)] = True
    return new_dots

def process(content):
    dots, folds = content.strip().split("\n\n")
    dots = {tuple(map(int, dot.split(","))): True for dot in dots.split("\n")}
    folds = [fold.split("=") for fold in folds.split("\n")]
    folds = [(fold[0][-1], int(fold[1])) for fold in folds]
    for (side, position) in folds:
        dots = perform_fold(dots, side, position)
    max_x = max([x for (x, _) in dots.keys()])
    max_y = max([y for (_, y) in dots.keys()])
    sheet = []
    for y in range(max_y+1):
        row = ""
        for x in range(max_x+1):
            if (x, y) in dots:
                row += "#"
            else:
                row += "."
        sheet.append(row)
    return "\n".join(sheet)

assert process("""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""") == """#####
#...#
#...#
#...#
#####"""

assert process(content) == """\
#....###...##..###..###..####..##..###.
#....#..#.#..#.#..#.#..#.#....#..#.#..#
#....#..#.#....#..#.#..#.###..#....###.
#....###..#.##.###..###..#....#....#..#
#....#.#..#..#.#....#.#..#....#..#.#..#
####.#..#..###.#....#..#.####..##..###."""

print(process(content))
