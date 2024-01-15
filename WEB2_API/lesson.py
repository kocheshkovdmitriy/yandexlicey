import random
board = [[random.randint(0, 100) for i in range(4)] for _ in range(4)]

print(*board, sep='\n')
def check_board(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == 0:
                return False
    for x in range(4):
        for y in range(3):
            if board[x][y] == board[x][y + 1] or board[y][x] == board[y + 1][x]:
                return False
    return True


print(check_board(board))