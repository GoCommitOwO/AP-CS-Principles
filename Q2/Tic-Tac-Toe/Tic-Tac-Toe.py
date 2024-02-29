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
    current_player = "X" if current_player == "ඞ" else "ඞ"


def get_player_color():
    return "red" if current_player == "X" else "blue"


def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == current_player or
                board[i] == board[i + 3] == board[i + 6] == current_player):
            return True
    if (board[0] == board[4] == board[8] == current_player or
            board[2] == board[4] == board[6] == current_player):
        return True
    return False


def show_winner_message():
    messagebox.showinfo("Winner", f"Player {current_player} wins!")
    #using an "isEqual(val1, val2) function to count the number of Xs on the board
    xcount = 0
    suscount = 0
    for i in range(9):
        if isEqual(str(board[i-1].upper()), "X"):
            xcount += 1
        elif isEqual(str(board[i-1].upper()), "ඞ"):
            suscount += 1
    print("X count: " + str(xcount))
    print("\nSus count: " + str(suscount))


def isEqual(val1, val2):
    return val1 == val2

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
            button = tk.Button(root, text="", font=('Helvetica', 48), width=3, height=1,
                               command=lambda i=i, j=j: click(i, j))
            button.grid(row=i, column=j)
            buttons.append(button)

    root.mainloop()
