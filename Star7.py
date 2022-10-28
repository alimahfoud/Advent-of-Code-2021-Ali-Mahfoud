with open("/home/alimahfoud24/ALI/inputDay4.txt") as file:
    Number_to_Draw = [int(x) for x in file.readline().strip('\n').split(',')]
    bingo_boards = []
    while file.readline():
        bingo_board = []
        for i in range(5):
            bingo_board.extend(
                [int(x) for x in file.readline().strip('\n').split(' ') if x != ''])
        bingo_boards.append(bingo_board)


def Winner(bingo_board):
    x = 0
    for i in range(5):
        if bingo_board[x] + bingo_board[x+1] + bingo_board[x+2] + bingo_board[x+3] + bingo_board[x+4] == 500:
            return True
        x += 5

    x = 0
    for i in range(5):
        if bingo_board[x] + bingo_board[x+5] + bingo_board[x+10] + bingo_board[x+15] + bingo_board[x+20] == 500:
            return True
    x += 1

    return False


found = False
while found == False:
    n = Number_to_Draw[0]
    Number_to_Draw = Number_to_Draw[1:]
    for bingo_board in bingo_boards:
        for i in range(len(bingo_board)):
            if bingo_board[i] == n:
                bingo_board[i] = 100
    for bingo_board in bingo_boards:
        if Winner(bingo_board):
            total = sum([t for t in bingo_board if t != 100])
            Result = total*n
            print('Congrats,the score is: ', Result)
            found = True
