# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(0, 100, 200, 100, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(100, 200, 100, 0, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

c.create_oval(50, 10, 150, 110, width=2)
c.create_oval(10, 120, 190, 190, fill='grey70', outline='white')
 
root.mainloop()