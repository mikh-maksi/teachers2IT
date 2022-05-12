# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white') # Размер и цвет холста
c.pack()
 
c.create_line(3, 3, 200, 200)
 
c.create_line(3, 3, 200, 3, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(3, 3, 3, 200, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")


c.create_rectangle(60, 80, 140, 190, fill='yellow', outline='green',
                    width=3, activedash=(5, 4))
 
root.mainloop()