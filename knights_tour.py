import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def create_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print(row)


def is_valid_move(board, x, y):
    if x >= 0 and x < len(board) and y >= 0 and y < len(board) and board[x][y] == 0:
        return True
    return False


def knight_tour(board, x, y, move_count, start_x, start_y):
    if move_count == len(board) ** 2:
        board[x][y] = move_count
        if (x + 2, y + 1) == (start_x, start_y) or (x + 2, y - 1) == (start_x, start_y) or \
                (x - 2, y + 1) == (start_x, start_y) or (x - 2, y - 1) == (start_x, start_y) or \
                (x + 1, y + 2) == (start_x, start_y) or (x + 1, y - 2) == (start_x, start_y) or \
                (x - 1, y + 2) == (start_x, start_y) or (x - 1, y - 2) == (start_x, start_y):
            return "Closed Tour"
        else:
            return "Open Tour"

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    for move in moves:
        next_x = x + move[0]
        next_y = y + move[1]
        if is_valid_move(board, next_x, next_y):
            board[x][y] = move_count
            result = knight_tour(board, next_x, next_y, move_count + 1, start_x, start_y)
            if result:
                return result
            board[x][y] = 0

    return False


def run_game():
    n = int(size_entry.get())
    start_x = int(x_entry.get())
    start_y = int(y_entry.get())

    board = create_board👎
    result = knight_tour(board, start_x, start_y, 1, start_x, start_y)
    print_board(board)

    root.destroy()

    root2 = tk.Tk()
    root2.title("Knight's Tour")
    font = ("Arial", 30)
    for i in range(n):
        for j in range(n):
            label = tk.Label(root2, text=str(board[i][j]), font=font, width=4, height=2, bg="light blue", bd=2,
                             relief="solid")
            label.grid(row=i, column=j)
    result_label = tk.Label(root2, text=result, font=font, bg="light pink", bd=2, relief="solid")
    result_label.grid(row=n, column=0, columnspan=n)


root = tk.Tk()
root.title("KNIGHTS TOUR")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
image = Image.open(r"C:\Users\YADA LIKHITHA\Desktop\image1.jpeg")
image = image.resize((screen_width, screen_height), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.image = photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)


size_label = tk.Label(root, text="BOARD SIZE:",font=30)
size_label.grid(row=0, column=0,padx=5,pady=5)
size_entry = tk.Entry(root,bg='light blue', font =30)
size_entry.grid(row=0, column=1,padx=5, pady=5,ipadx=100,ipady=20)

x_label = tk.Label(root, text="X COORDINATE:",font=30)
x_label.grid(row=1, column=0,padx=5,pady=5)
x_entry = tk.Entry(root,bg='light green', font =30)
x_entry.grid(row=1, column=1,padx=5, pady=5,ipadx=100,ipady=20)

y_label = tk.Label(root, text="Y COORDINATE:",font=30)
y_label.grid(row=2, column=0,padx=5,pady=5)
y_entry = tk.Entry(root,bg='light pink', font =30)
y_entry.grid(row=2, column=1,padx=5, pady=5,ipadx=100,ipady=20)

submit_button = tk.Button(root, text="SUBMIT", command=run_game,font= 60 , bg= "light yellow")
submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
