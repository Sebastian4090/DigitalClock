from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.iconbitmap("icon.ico")

def time():
    string = strftime("%H:%M:%S %p")
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root, font=("DS-DIGI.TTF", 80), background = "black", foreground ="red")
Label.pack(anchor="center")



time()


root.mainloop()