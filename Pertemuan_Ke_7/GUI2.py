import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
top.title("pinkky")

C = tk.Canvas(top, bg= "pink", height= 250, width= 300)
coord = 10,50,240,280
arc = C.create_arc(coord, start=0, extent=150, fill="black")
C.pack()

checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()

checkButton1 = tk.Checkbutton(top, text= "music", variable= checkVar1)
checkButton2 = tk.Checkbutton(top, text= "music", variable= checkVar2)

checkButton1.pack()
checkButton2.pack()

top.mainloop()