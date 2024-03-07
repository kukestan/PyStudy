from tkinter import *
import tkinter as tk
from turtle_lib import taiji
from datetime import datetime
import public.log as log

root = tk.Tk()
root.title("rudy")
frm = tk.Frame(root) # type: ignore
frm.grid()
tk.Label(frm, text="Hello World!").grid(column=0, row=2)
#tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
tk.Button(frm, text="Quit", command=taiji.draw).grid(column=1, row=0)
root.mainloop()