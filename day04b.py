import re

with open("day04.txt") as f:
    content = f.read()

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def bingo(board):
    hit = ['x'] * len(board[0])
    hits_rows = [row == hit for row in board]
    flipped = transpose(board)
    hits_columns = [column == hit for column in flipped]
    return any(hits_rows) or any(hits_columns)

assert bingo([['x', 'x']])
assert bingo([['0', 'x'], ['1', 'x']])

def all_bingo(boards):
    return all(map(bingo, boards))

def mark(board, mark):
    new_board = []
    for line in board:
        new_line = []
        for value in line:
            if value == mark:
                new_line.append("x")
            else:
                new_line.append(value)
        new_board.append(new_line)
    return new_board

assert mark([['1', '2'], ['2', '3']], '2') == [['1', 'x'], ['x', '3']]

def calculate(board, draw):
    sum = 0
    for line in board:
        for value in line:
            if value != 'x':
                sum += int(value)
    return sum * int(draw)

def process(content):
    [draws, *boards] = content.split("\n\n")
    draws = draws.split(",")
    boards = [board.strip() for board in boards]
    boards = [board.split("\n") for board in boards]
    boards = [[re.split("\s+", line.strip()) for line in board] for board in boards]
    for draw in draws:
        for (index, board) in enumerate(boards):
            board = mark(board, draw)
            boards[index] = board
            if all_bingo(boards):
                return calculate(board, draw)

assert process("""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""") == 1924

assert process(content) == 8224

print(process(content))
