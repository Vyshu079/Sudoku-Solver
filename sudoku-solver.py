
def solver(board):

    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solver(board):
                return True

            board[row][col] = 0

    return False


def valid(board, pos, num):

    # Check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(boaqrd[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")

