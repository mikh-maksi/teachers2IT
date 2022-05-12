# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

root.title("My Name Application")


c.create_line(0, 100, 200, 100, fill='red',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(100, 200, 100, 0, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

c.create_text(100, 100, text="My Name is,\nMikhail\n", 
                justify=CENTER, font="Verdana 20")

c.create_rectangle(0, 0, 200, 53, fill='lightblue')


c.create_rectangle(0, 100, 200, 200, fill='yellow')

c.create_oval(10, 10, 50, 50, fill='yellow', outline='white')
root.mainloop()