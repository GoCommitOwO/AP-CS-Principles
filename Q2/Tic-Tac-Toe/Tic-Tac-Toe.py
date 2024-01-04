import tkinter as tk
from tkinter import messagebox


def click(i, j):
    index = 3 * i + j

    if board[index] == "":
        board[index] = current_player
        update_button_text(buttons[index])

        if check_winner():
            show_winner_message()
            reset_game()
        elif "" not in board:
            show_tie_message()
            reset_game()
        else:
            switch_player()


def update_button_text(button):
    button.config(text=current_player, state=tk.DISABLED, disabledforeground=get_player_color())


def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"


def get_player_color():
    return "red" if current_player == "X" else "blue"


def check_winner():
    # Check rows for a win
    for i in range(3):
        if all(board[i * 3 + j] == current_player for j in range(3)):
            return True

    # Check columns for a win
    for i in range(3):
        if all(board[i + j * 3] == current_player for j in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i] == current_player for i in range(0, 9, 4)) or all(
            board[i] == current_player for i in range(2, 7, 2)):
        return True

    return False


def show_winner_message():
    messagebox.showinfo("Winner", f"Player {current_player} wins!")


def show_tie_message():
    messagebox.showinfo("Tie", "It's a tie!")


def reset_game():
    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", state=tk.NORMAL)


if __name__ == "__main__":
    current_player = "X"
    board = [""] * 9

    root = tk.Tk() # this line is from chatgpt
    root.title("Tic-Tac-Toe")

    buttons = []

    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text="", font=('Helvetica', 24), width=3, height=1,
                               command=lambda i=i, j=j: click(i, j))
            button.grid(row=i, column=j)
            buttons.append(button)

    root.mainloop()