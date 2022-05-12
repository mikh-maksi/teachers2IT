# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

root.title("Picture Application")

c.create_rectangle(0, 0, 200, 74, fill='blue')
c.create_rectangle(0, 142, 200, 200, fill='yellow', outline='yellow')
c.create_oval(5, 9, 45, 49, fill='black', outline='white')

root.mainloop()