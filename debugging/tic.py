#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Return the player symbol if there's a winner

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # Return the player symbol if there's a winner

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Return the player symbol if there's a winner

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Return the player symbol if there's a winner

    return None  # Return None if there's no winner

def is_board_full(board):
    for row in board:
        if " " in row:
            return False  # If any cell is empty, the board is not full
    return True  # If all cells are occupied, the board is full

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print("Player " + winner + " wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input! Row and column values must be between 0 and 2.")

tic_tac_toe()
