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

c.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')

c.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
c.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
c.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
c.create_arc(10, 10, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)
 
root.mainloop()