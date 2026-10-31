import tkinter as tk
import random
from func import next_generation

root = tk.Tk()
root.title("life game")
root.geometry("800x900")
root.resizable(False, False)

N = 50 
CELL_SIZE = 800//N
running=False

field = [[0 for _ in range(N)] for _ in range(N)]
canvas = tk.Canvas(
    root, 
    width = 800,
    height=800,
    bg='white',
    highlightthickness=0)
canvas.pack(side=tk.TOP)

def draw_field():
    for i in range(N):
        for j in range(N):
            color = "black" if field[i][j] == 1 else "white"

            canvas.itemconfig(
                rectangles[i][j],
                fill=color
            )

def update():
    global running
    global field
    if not running:
        return

    field=next_generation(field)
    draw_field()

    root.after(30, update)

def start():
    global running
    if not running:
        running=True
        update()

def pause():
    global running
    running = False

def clear():
    global field

    field = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
           canvas.itemconfig(
                        rectangles[i][j],
                        fill="white"
                       ) 
def random_pattern():
    global field

    field = [[random.choice([0,1]) for _ in range(N)] for _ in range(N)]

    color = "black" if field[i][j] == 1 else "white"
    canvas.itemconfig(
                    rectangles[i][j],
                    fill=color
                )


start_button=tk.Button(root, text="Start", command=start)
start_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                  padx = 10, pady=10)
pause_button=tk.Button(root, text="Pause", command=pause)
pause_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                  padx = 10, pady=10)
clear_button=tk.Button(root, text="Clear", command=clear)
clear_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                  padx = 10, pady=10)
random_button=tk.Button(root, text="Random", command=random_pattern)
random_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                  padx = 10, pady=10)    
            
rectangles = []
for i in range(N):
    row=[]
    for j in range(N):
        x1 = j*CELL_SIZE
        y1 = i*CELL_SIZE

        rect = canvas.create_rectangle(
            x1, y1,
            x1+CELL_SIZE, y1+CELL_SIZE,
            fill="white",
            outline="black"
        )
        row.append(rect)
    rectangles.append(row)    

def toggle_cell(event):
    j = event.x // CELL_SIZE
    i = event.y // CELL_SIZE

    if 0 <= i < N and 0 <= j < N:
        field[i][j] = 1 - field[i][j]

        canvas.itemconfig(
            rectangles[i][j],
            fill="black" if field[i][j] else "white"
        )

canvas.bind("<Button-1>", toggle_cell)

tk.mainloop()