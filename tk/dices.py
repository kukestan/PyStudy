from tkinter import * # type: ignore
from random import *  # type: ignore
import tkinter.messagebox
rudy_dice = 1
rosser_dice = 1
rudy_lock = True
rosser_lock = True

def init():
    global rudy_dice
    global rosser_dice
    global rudy_lock
    global rosser_lock
    rudy_dice = 1
    rosser_dice = 1
    rudy_lock = False
    rosser_lock = False
    diceA.config(fg = 'blue')
    diceB.config(fg = 'blue')
    vs.config(text = "VS", fg = "black")

def update():
    global rudy_dice
    global rosser_dice
    global rudy_lock
    global rosser_lock
    if rudy_lock and rosser_lock:
        if rudy_dice > rosser_dice:
            vs.config(text = "赢", fg = "red")
        elif rudy_dice < rosser_dice:
            vs.config(text = "输", fg = "blue")
        elif rudy_dice == rosser_dice:
            vs.config(text = "平", fg = "yellow")

def print_dice(dice):
    return ' %s ' % str(dice)

def btnAPress():
    global rudy_dice
    global rudy_lock
    if not rudy_lock:
        diceA.delete(0.0, END)
        rudy_dice = randint(1, 6)
        diceA.insert(END, print_dice(rudy_dice))
        diceA.config(fg = 'red')
        rudy_lock = True
        update()
    else:
        a = tkinter.messagebox.showinfo("警告", "请先点击开始按钮")

def btnBPress():
    global rosser_dice
    global rosser_lock
    if not rosser_lock:
        diceB.delete(0.0, END)
        rosser_dice = randint(1, 6)
        diceB.insert(END, print_dice(rosser_dice))
        diceB.config(fg = 'red')
        rosser_lock = True
        update()
    else:
        a = tkinter.messagebox.showinfo("警告", "请先点击开始按钮")
#定义窗口
window = Tk()
window.title("骰子")
# 调整窗口大小和位置，单位是像素
width, height = 800, 400
place_x, place_y = 500, 500 #位置以屏幕左上角为起始点（0,0）
window.geometry(f'{width}x{height}+{place_x}+{place_y}')

#定义骰子A
diceA = Text(window, width = 3, height = 1)
diceA.delete(0.0, END)
diceA.insert(END, print_dice(rudy_dice))
diceA.place(x = 100, y = 100)
diceA.config(font = "courier 100", bg = 'gray', fg = 'blue')

vs = Label(window, text = "")
vs.place(x = 350, y = 150)
vs.config(font = "courier 50")

#定义骰子B
diceB = Text(window, width = 3, height = 1)
diceB.delete(0.0, END)
diceB.insert(END, print_dice(rosser_dice))
diceB.place(x = 450, y = 100)
diceB.config(font = "courier 100", bg = 'gray', fg = 'blue')

#定义按钮A
btnA = Button(window, text = "Rudy", command = btnAPress)
btnA.place(x = 170, y = 300)
btnA.config(font = "courier 20")

#定义按钮B
btnB = Button(window, text = "Rosser", command = btnBPress)
btnB.place(x = 500, y = 300)
btnB.config(font = "courier 20")

#定义开始按钮
btnStart  = Button(window, text = "开始", command = init)
btnStart.place(x = 350, y = 50)
btnStart.config(font = "courier 20")
#btnStart.pack()
window.mainloop()
