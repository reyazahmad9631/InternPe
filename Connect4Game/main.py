import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
PLAYER1 = 1
PLAYER2 = 2
EMPTY = 0

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = PLAYER1
        self.buttons = [tk.Button(root, text="Drop", command=lambda col=col: self.drop_piece(col))
                        for col in range(COLS)]
        for col, button in enumerate(self.buttons):
            button.grid(row=0, column=col)
        self.labels = [[tk.Label(root, text=" ", width=6, height=3, relief="ridge", bg="white")
                        for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.labels[r][c].grid(row=r+1, column=c)
        self.update_board()

    def update_board(self):
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] == PLAYER1:
                    self.labels[r][c].config(bg="aqua")
                elif self.board[r][c] == PLAYER2:
                    self.labels[r][c].config(bg="black")
                else:
                    self.labels[r][c].config(bg="white")

    def drop_piece(self, col):
        for r in range(ROWS-1, -1, -1):
            if self.board[r][col] == EMPTY:
                self.board[r][col] = self.turn
                if self.check_winner(self.turn):
                    self.update_board()
                    winner = "Player 1" if self.turn == PLAYER1 else "Player 2"
                    messagebox.showinfo("Connect Four", f"{winner} wins!")
                    self.reset_game()
                elif all(self.board[r][c] != EMPTY for r in range(ROWS) for c in range(COLS)):
                    messagebox.showinfo("Connect Four", "It's a draw!")
                    self.reset_game()
                else:
                    self.turn = PLAYER1 if self.turn == PLAYER2 else PLAYER2
                break
        self.update_board()

    def check_winner(self, piece):
        # Check horizontal locations for win
        for c in range(COLS-3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLS):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLS-3):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLS-3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

        return False

    def reset_game(self):
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = PLAYER1
        self.update_board()

def main():
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()

if __name__ == "__main__":
    main()
