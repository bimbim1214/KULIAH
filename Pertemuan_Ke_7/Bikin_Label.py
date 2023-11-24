import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

L1 = tk.Label(top,text= "user Name" )
L1.grid(row= 0, column=0)

L1.pack()

#input  data
E1 = tk.Entry(top, bd=5)
E1.grid(row=1, column=1)

E1.pack()

top.mainloop()