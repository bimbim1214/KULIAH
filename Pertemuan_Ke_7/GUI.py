import tkinter
import tkinter.messagebox
top  = tkinter.Tk()
def helloCollback():
    tkinter.messagebox.showinfo("Hello Python", "Hello word")
    
B = tkinter.Button(top, text= "hello", command=helloCollback)
B.pack()

top.mainloop()