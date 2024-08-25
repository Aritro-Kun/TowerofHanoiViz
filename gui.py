import tkinter as tk
import time

#Creating the window, for the gui features to exist
root = tk.Tk()
root.title("Tower of Hanoi")
root.geometry("800x600")

top_label=tk.Label(root, text="Tower of Hanoi", font=("Arial", 24))
top_label.pack(pady=20)

input_frame=tk.Frame(root)
input_frame.pack(pady=20)

input_label=tk.Label(input_frame, text="no. of Rings: ", font=("Arial", 10))
input_label.grid(row=0, column=0, padx=5)

input_entry=tk.Entry(input_frame, width=5, font=("Arial", 10))
input_entry.grid(row=0, column=1, padx=5)

max_label=tk.Label(input_frame, text="^^ can process a maximum of 7rings.", font=("Arial", 10))
max_label.grid(row=0, column=2, padx=5)

vis_button = tk.Button(input_frame, text="Visualise", font=("Arial", 10), command=lambda: visualise_button())
#NOTE! in the command section, the lambda function is just a sugarcoat to check whether the button orks or not. and importantly, the function which is supposed to get trigerred will consist of the whole logic behind the visualisation.
vis_button.grid(row=1, columnspan=4, padx=10, pady=(10, 10))

canvas=tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack(pady=20)

peg_x_coordinates = [150, 300, 450]
for i in peg_x_coordinates:
    canvas.create_line(i, 100, i, 250, width=5)

#Starting to define the funbctions, innit.

def visualise_button(): #the function which has to get trigerred when the visualise button gets clicked.
    num_rings=int(input_entry.get())
    if(num_rings>7):
        print("Max 6 rings are supported.")
        return
    pegs=[[i for i in range(num_rings, 0, -1)],[],[]]
    draw_pegs(pegs, num_rings)
    hanoi_algo(num_rings, 0, 1, 2, pegs)



def draw_pegs(pegs, num_rings):
    canvas.delete("all")
    for i in peg_x_coordinates:
        canvas.create_line(i, 100, i, 250, width=5)
    for peg_index, peg in enumerate(pegs):
        for ring_index, ring in enumerate(peg):
            ring_width=ring*20
            ring_x_centre=peg_x_coordinates[peg_index]
            ring_y_centre=250-(ring_index*20)
            canvas.create_rectangle(ring_x_centre - ring_width // 2, ring_y_centre-10, ring_x_centre+ring_width // 2, ring_y_centre+10, fill="black")
    root.update()


def hanoi_algo(n, initial, auxiliary, end, pegs):
    if(n==0):
        return
    
    time.sleep(0.75)
    root.update_idletasks()

    hanoi_algo(n-1, initial, end, auxiliary, pegs)

    ring=pegs[initial].pop()
    pegs[end].append(ring)
    draw_pegs(pegs, len(pegs[0])+len(pegs[1])+len(pegs[2]))

    time.sleep(0.75)
    root.update_idletasks()

    hanoi_algo(n-1, auxiliary, initial, end, pegs)


root.mainloop()
