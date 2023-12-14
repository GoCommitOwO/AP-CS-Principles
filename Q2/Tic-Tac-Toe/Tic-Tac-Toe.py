import tkinter as tk
from tkinter import messagebox, simpledialog


def click(i, j):
    index = 3 * i + j

    if board[index] == "":
        board[index] = current_player
        update_button_text(buttons[index])

        if check_winner == True:
            show_winner_message()
            reset_game()
        elif "" not in board:
            show_tie_message()
            reset_game()
        else:
            switch_player()


def update_button_text(button):
    button.config(text=current_player, state=tk.DISABLED, disabledforeground=get_player_color()) #disabled foreground came from mr gpt-3.5


def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"


def get_player_color():
    return "red" if current_player == "X" else "blue"


def check_winner():
    # check rows (i*3, i*3+1...), columns (i, i+3...), and diagonals (0,4...) for a win
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


def show_tie_message():
    messagebox.showinfo("Tie", "It's a tie!")


def reset_game():
    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", state=tk.NORMAL)




if __name__ == "__main__": # <---- cheat-gpt bc i forgor how to do this

    # make a pop-up window to select player
    #choose_starting_player()
    # boom did it

    # LMAO NOPE i lied, it didn't work
    # bog standard it is
    current_player = "X"

    board = [""] * 9

    root = tk.Tk() # <--- cheat gpt
    root.title("Tic-Tac-Toe") # <--- not cheat gpt

    buttons = []

    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text="", font=('Helvetica', 24), width=3, height=1,
                               command=lambda i=i, j=j: click(i, j))
                        # root and command=lambda came from chatgpt

            button.grid(row=i, column=j)
            buttons.append(button)

    root.mainloop()
