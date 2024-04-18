# Костыль, чтобы интерфейс не был размытым
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})", width=100)
        btn.grid(row=r, column=c)
 
root.mainloop()