import tkinter as tk

r = tk.Tk()
r.minsize(400,400)
canvas = tk.Canvas(r, width=400, height=400)
# main building
canvas.create_rectangle(100, 100, 300, 350, fill='skyblue')
# door
canvas.create_rectangle(180, 275, 220, 350, fill='light green')
# roof
canvas.create_polygon(100, 100, 300, 100, 200, 30, fill='skyblue', outline='black')
# left window
canvas.create_rectangle(130, 150, 170, 200, fill='yellow')
# right window
canvas.create_rectangle(230, 150, 270, 200, fill='yellow')
#door knob
canvas.create_oval(205, 308, 215, 318, fill='black')

canvas.pack()
r.mainloop()