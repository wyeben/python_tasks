import tkinter as tk
from tkinter import messagebox, colorchooser
import random


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def on_button_click(row, col):
    global current_player

    if board[row][col] == " " and not check_winner(board, current_player) and not is_board_full(board):
        buttons[row][col].config(text=current_player, fg=current_color[current_player])
        board[row][col] = current_player

        if check_winner(board, current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins! Congratulations!")
            play_again()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            play_again()
        else:
            current_player = "O" if current_player == "X" else "X"


def on_open_button_click():
    row = int(row_entry.get()) - 1
    col = int(col_entry.get()) - 1

    if 0 <= row < 3 and 0 <= col < 3:
        on_button_click(row, col)
    else:
        messagebox.showwarning("Invalid Input", "Invalid row and column. Please enter numbers between 1 and 3.")


def reset_board():
    global board
    board = create_board()
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", fg="black")


def change_random_color():
    global current_color, bg_color

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    new_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

    current_color = {"X": new_color, "O": new_color}
    bg_color = new_color

    set_text_color()
    root.configure(bg=bg_color)
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(bg=bg_color)
    color_label.config(bg=bg_color, text="Current Background Color")


def set_text_color():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(fg=current_color[board[i][j]])


def play_again():
    choice = messagebox.askyesno("Play Again", "Do you want to play again?")
    if choice:
        reset_board()
    else:
        root.quit()


current_player = "X"
current_color = {"X": "blue", "O": "red"}
bg_color = "white"
board = create_board()

root = tk.Tk()
root.title("Americana Tic-Tac-Toe")

buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=("Helvetica", 24),
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

row_label = tk.Label(root, text="Row:")
row_label.grid(row=3, column=0)
row_entry = tk.Entry(root)
row_entry.grid(row=3, column=1)

col_label = tk.Label(root, text="Column:")
col_label.grid(row=3, column=2)
col_entry = tk.Entry(root)
col_entry.grid(row=3, column=3)

open_button = tk.Button(root, text="Open", command=on_open_button_click)
open_button.grid(row=3, column=4)

change_color_button = tk.Button(root, text="Change Random Color", command=change_random_color)
change_color_button.grid(row=4, column=0, columnspan=5)

color_label = tk.Label(root, text="Current Background Color", bg=bg_color)
color_label.grid(row=5, column=0, columnspan=5)

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=6, column=0, columnspan=2)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=6, column=3, columnspan=2)

root.mainloop()
