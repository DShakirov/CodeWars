def is_winner(board, n):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] == n:
            return True
        if board[0][i] == board[1][i] == board[2][i] == n:
            return True
        if board[0][0] == board[1][1] == board[2][2] == n:
            return True
    return False    

def is_solved(board):
    # check winner:
    if is_winner(board, 1):
        return 1
    elif is_winner(board, 2):
        return 2
    # check tie
    for i in board:
        if 0 in i:
            return -1
    return 0

print(is_solved([[0, 0, 1], [0, 1, 2], [2, 1, 0]]))
