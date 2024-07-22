import tkinter as tk 
from time import strftime

root = tk.Tk()
root.title("Ditial Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=("ds-digital", 80), background = "black", foreground = "aqua")
label.pack(anchor='center')

time()

root.mainloop()
