"""
Created by: Shingai Dzinotyiweyi

Task 3: N-Queens Problem
Solve the classic N-Queens problem where the goal is to place N queens on an N x N
chessboard such that no two queens threaten each other

Objectives:
✅ - Represent the chessboard as a 2D array.
✅ - Use backtracking to place queens one by one in safe positions.
✅ - Ensure that no two queens are on the same row, column, or diagonal
"""

chessboard = [[" " for _ in range(8)] for _ in range(8)]
answer = 0

def print_chessboard():
    """
    Prints the chessboard in a user-friendly format
    """
    for row in chessboard:
        print(row)
    print("\n\n")

print("Before:\n")
print_chessboard()

def check_safety(row, col):
    """
    Checks if the chessboard has any safe squares that
    are not occupied by a queen.
    """

    # Check Horizontally: e.g. [0][0] - [0][7] ⬅️➡️
    for i in range(row):
        if chessboard[row][i] == 'Q':
            return False

    # Check Vertically: e.g. [0][0] - [7][0] ⬆️⬇️
    for i in range(row):
        if chessboard[i][col] == 'Q':
            return False

    # Check Diagonally Upward (Left): e.g. [7][7] - [0][0] ↖️
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] == 'Q':
            return False

    # Check Diagonally Upward (Right): e.g. [7][0] - [0][7] ↗️
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if chessboard[i][j] == 'Q':
            return False

    return True

def add_queen(row):
    """
    Adds a new queen on the safe squares of the chessboard,
    then recursively backtracks until reaching the end of
    board.
    """
    global answer

    if row == 8:
        answer += 1
        print(f"After: {answer} Found\n")
        print_chessboard()
        return

    for col in range(8):
        if check_safety(row, col):
            chessboard[row][col] = 'Q'
            add_queen(row + 1)
            chessboard[row][col] = ' '


add_queen(0)
print("Total solutions:", answer)