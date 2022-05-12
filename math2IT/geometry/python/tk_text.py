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

c.create_text(100, 100, text="Hello World,\nPython\nand Tk", 
                justify=CENTER, font="Verdana 20")
c.create_text(200, 200, text="About this", 
                anchor=SE, fill="grey")

root.mainloop()