# Name: Final Project
# Purpose: Tic Tac Toe Final Project
#
# Author: theresaf
#
# Created: 12/4/2023
# Copyright: (c) theresaf 2023

# Importing module and file handling functions
import os.path

#Reading and writing to text file
def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return None


# Tic Tac Toe Game
# Title Intro
print("Let's Play Tic Tac Toe")

# 9x9 gameboard
board = ["-" for _ in range(9)]

def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("_________")

# Player inputs
players = ["X", "O"]
current_player = players[0]
winner = None
game_running = True

def player_input(board, player):
    while True:
        try:
            inp = int(input(f"Player {player}, choose a number from 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == "-":
                board[inp - 1] = player
                break
            else:
                print("Spot already taken or invalid input. Choose again.")
        except ValueError:
            print("Invalid input. Choose a number.")

# Check if win or tie
def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "-":
            return True, board[condition[0]]
    if "-" not in board:
        return True, None
    return False, None

# Gameplay
while game_running:
    display_board(board)
    player_input(board, current_player)
    win, winner = check_win(board)
    if win:
        display_board(board)
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a tie!")
        game_running = False
    else:
        current_player = "O" if current_player == "X" else "X"

# Unit test for one of the functions
def test_check_win():
    test_board = ["X", "X", "X", "-", "-", "-", "-", "-", "-"]
    assert check_win(test_board) == (True, "X")


# Storing game status
file_name = "final.txt"
file_path = f"./final/{file_name}"  

# Storing game status in the file
game_status = {
    "board": board,
    "current_player": current_player,
    "winner": winner,
    "game_running": game_running
}

# Writing game status to the file
write_to_file(file_path, str(game_status))

# Reading game status from the file
stored_game_status = read_from_file(file_path)
if stored_game_status:
    # Perform necessary operations with the stored game status
    # ...
    pass
test_check_win()


