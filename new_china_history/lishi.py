import tkinter as tk
import time
from data import *

# 创建主窗口
window = tk.Tk()
window.title('进度条')
# 调整窗口大小和位置，单位是像素
width, height = 1800, 400
place_x, place_y = 0, 500 #位置以屏幕左上角为起始点（0,0）
window.geometry(f'{width}x{height}+{place_x}+{place_y}')

# 设置下载进度条
tk.Label(window, text='下载进度:', ).place(x=50, y=60)
canvas = tk.Canvas(window, width=1500, height=200, bg="white")
canvas.place(x=0, y=60)


# 显示下载进度
def progress():
    startX = 0
    for i in range(0, len(zongshuji) - 1):
        endx = startX + month_diff(zongshuji[i], zongshuji[i + 1])
        str = shijian[zongshuji[i]]
        print(f'i = {i}, startX = {startX}, endx = {endx}, str = {str}')
        # 填充进度条
        fill_line = canvas.create_rectangle(startX, 0, endx, 50, width=0, fill = color[i])
        for j in range(startX, endx + 1):
            canvas.coords(fill_line, (startX, 0, j, 50))
            words = canvas.create_text(startX + 10, 25, text = str, width = 20)
            window.update()
            time.sleep(0)  # 控制进度条流动的速度
        fill_line1 = canvas.create_rectangle(startX, 50, endx, 100, width=0, fill = color[i])
        for j in range(startX, endx + 1):
            canvas.coords(fill_line1, (startX, 50, j, 100))
            words1 = canvas.create_text(startX + 10, 75, text = str, width = 20)
            window.update()
            time.sleep(0)  # 控制进度条流动的速度
        print(f'zongshuji[i] = {zongshuji[i]}, 画完')
        print(f'j = {j}, 画完')
        startX = endx

print(len(zongshuji))
btn_download = tk.Button(window, text='启动进度条', command=progress)
btn_download.place(x=400, y=105)

window.mainloop()