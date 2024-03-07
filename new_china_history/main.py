from tkinter import *
from datetime import  datetime, timedelta, date
from time import sleep
#自定义常量
from data import *
from dateutil.relativedelta import *

#创建主窗口
window = Tk()
window.title('新中国历史')
#调整窗口大小和位置，单位是像素
width, height, place_x, place_y = 1600, 700, 100, 300
window.geometry(f'{width}x{height}+{place_x}+{place_y}')

#信息框，显示日期和重大事件
msg = Text(window, width = 50, height = 1)
msg.delete(0.0, END)
msg.insert(END, '')
msg.place(x = 0, y = 0)
msg.config(font = "courier 20", bg = 'gray', fg = 'blue')

#总书记
lab_secretry = Label(window, text = "总书记")
lab_secretry.place(x = 0, y = 50)
lab_secretry.config(font = "courier 20")
secretry = Canvas(window, width=1500, height=50, bg="white")
secretry.place(x=0, y=100)
#国家主席
lab_secretry = Label(window, text = "国家主席")
lab_secretry.place(x = 0, y = 150)
lab_secretry.config(font = "courier 20")
chairman = Canvas(window, width=1500, height=50, bg="white")
chairman.place(x=0, y=200)
#军委主席
lab_military = Label(window, text = "中央军委主席")
lab_military.place(x = 0, y = 250)
lab_military.config(font = "courier 20")
military = Canvas(window, width=1500, height=50, bg="white")
military.place(x=0, y=300)
#总理
lab_prime = Label(window, text = "总理")
lab_prime.place(x = 0, y = 350)
lab_prime.config(font = "courier 20")
prime = Canvas(window, width=1500, height=50, bg="white")
prime.place(x=0, y=400)
#政权
lab_state = Label(window, text = "政府")
lab_state.place(x = 0, y = 450)
lab_state.config(font = "courier 20")
state = Canvas(window, width=1500, height=50, bg="white")
state.place(x=0, y=500)
"""
我是分隔线--------------------------------------------------------------------------
"""



#界面更新函数
def progress():
    #总时间循环
#    for i in range((end - begin).days):
        #更新信息框
#        msg.delete(0.0, END)
#        msg.insert(END, begin + timedelta(days=i))

    #总书记历史更新
    startX = 0
    for i in range(0, len(TUP_SECRETRY) - 1):
        endx = startX + month_diff(TUP_SECRETRY[i], TUP_SECRETRY[i + 1])
        name = DICT_SECRETRY[TUP_SECRETRY[i]]
        #填充进度条
        if i == 0 or i == 5 or i == 11:
            secretry_line = secretry.create_rectangle(startX, 0, endx, 50, width=0, fill = 'red')
        else:
            secretry_line = secretry.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i % 7])
        for j in range(startX, endx + 1):
            secretry.coords(secretry_line, (startX, 0, j, 50))
            #显示当前人物
            msg.delete(0.0, END)
            msg.insert(END, f'{(TUP_SECRETRY[i] + relativedelta(months = +(j - startX))).year}-{(TUP_SECRETRY[i] + relativedelta(months = +(j - startX))).month}, {name}')
            #显示文字
            w = (endx- startX)
            if w > 80:
                f = "black 20"
            elif w > 60:
                f = "black 15"
            elif w > 50:
                f = "black 12"
            else:
                w = 12
                f = 'black 10'
            secretry.create_text((endx - startX) / 2 + startX, 25, text = name, width = w, font = f)
            #窗口更新
            window.update()
            #时间间隔
            sleep(0.02)
        startX = endx

    #国家主席历史更新
    startX = 0
    for i in range(0, len(DUP_CHAIRMAN) - 1):
        endx = startX + month_diff(DUP_CHAIRMAN[i], DUP_CHAIRMAN[i + 1])
        name = DICT_CHAIRMAN[DUP_CHAIRMAN[i]]
        #填充进度条
        if i == 0 or i == 2 or i == 5:
            chairman_line = chairman.create_rectangle(startX, 0, endx, 50, width=0, fill = 'white')
        else:
            chairman_line = chairman.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i % 7])
        for j in range(startX, endx + 1):
            chairman.coords(chairman_line, (startX, 0, j, 50))
            #显示当前人物
            msg.delete(0.0, END)
            msg.insert(END, f'{(DUP_CHAIRMAN[i] + relativedelta(months = +(j - startX))).year}-{(DUP_CHAIRMAN[i] + relativedelta(months = +(j - startX))).month}, {name}')
            #显示文字
            w = (endx- startX)
            if w > 80:
                f = "black 20"
            elif w > 60:
                f = "black 15"
            elif w > 50:
                f = "black 12"
            else:
                w = 12
                f = 'black 10'
            chairman.create_text((endx - startX) / 2 + startX, 25, text = name, width = w, font = f)
            #窗口更新
            window.update()
            #时间间隔
            sleep(0.02)
        startX = endx
        
    #中央军委主席历史更新
    startX = 0
    for i in range(0, len(DUP_MILITARY) - 1):
        endx = startX + month_diff(DUP_MILITARY[i], DUP_MILITARY[i + 1])
        name = DICT_MILITARY[DUP_MILITARY[i]]
        if i == 0:
            military_line = military.create_rectangle(startX, 0, endx, 50, width=0, fill = 'white')
        else:
            military_line = military.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i % 7])
        for j in range(startX, endx + 1):
            military.coords(military_line, (startX, 0, j, 50))
            #显示当前人物
            msg.delete(0.0, END)
            msg.insert(END, f'{(DUP_MILITARY[i] + relativedelta(months = +(j - startX))).year}-{(DUP_MILITARY[i] + relativedelta(months = +(j - startX))).month}, {name}')
            #显示文字
            w = (endx- startX)
            if w > 80:
                f = "black 20"
            elif w > 60:
                f = "black 15"
            elif w > 50:
                f = "black 12"
            else:
                w = 12
                f = 'black 10'
            military.create_text((endx - startX) / 2 + startX, 25, text = name, width = w, font = f)
            #窗口更新
            window.update()
            #时间间隔
            sleep(0.02)
        startX = endx

    #总理历史更新
    startX = 0
    for i in range(0, len(DUP_PRIME) - 1):
        endx = startX + month_diff(DUP_PRIME[i], DUP_PRIME[i + 1])
        name = DICT_PRIME[DUP_PRIME[i]]
        if i == 0 or i == 3:
            prime_line = prime.create_rectangle(startX, 0, endx, 50, width=0, fill = 'white')
        else:
            prime_line = prime.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i % 7])
        for j in range(startX, endx + 1):
            prime.coords(prime_line, (startX, 0, j, 50))
            #显示当前人物
            msg.delete(0.0, END)
            msg.insert(END, f'{(DUP_PRIME[i] + relativedelta(months = +(j - startX))).year}-{(DUP_PRIME[i] + relativedelta(months = +(j - startX))).month}, {name}')
            #显示文字
            w = (endx- startX)
            if w > 80:
                f = "black 20"
            elif w > 60:
                f = "black 15"
            elif w > 50:
                f = "black 12"
            else:
                w = 12
                f = 'black 10'
            prime.create_text((endx - startX) / 2 + startX, 25, text = name, width = w, font = f)
            #窗口更新
            window.update()
            #时间间隔
            sleep(0.02)
        startX = endx

    #政权历史更新
    startX = 0
    for i in range(0, len(DUP_STATE) - 1):
        endx = startX + month_diff(DUP_STATE[i], DUP_STATE[i + 1])
        name = DICT_STATE[DUP_STATE[i]]
        #显示当前人物
        msg.delete(0.0, END)
        msg.insert(END, f'{i}, {name}')
        #填充进度条
        if i == 0 or i == 2:
            state_line = state.create_rectangle(startX, 0, endx, 50, width=0, fill = 'white')
        else:
            state_line = state.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i % 7])
        for j in range(startX, endx + 1):
            state.coords(state_line, (startX, 0, j, 50))
            #secretry.create_text((endx - startX) / 2 + startX, 25, text = name, width = (endx- startX) / 4, font = "courier 20")
            w = (endx- startX)
            print(w)
            if w > 80:
                f = "black 20"
            elif w > 60:
                f = "black 15"
            elif w > 50:
                f = "black 12"
            else:
                w = 12
                f = 'black 10'
            if i == 1:
                w = 50
                f = 'black 10'
            state.create_text((endx - startX) / 2 + startX, 25, text = name, width = w, font = f)
            #窗口更新
            window.update()
            #时间间隔
            sleep(0)
        startX = endx

#标注时间线

#自动播放按钮
btn_play = Button(window, text='自动播放', command=progress)
btn_play.place(x=400, y=600)
window.mainloop()