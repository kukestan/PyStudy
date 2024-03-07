from turtle import *
from random import *
"""
抓住青色的球变红
"""
num = 5
long = 100
tBall = Turtle()
t = Turtle()


def drawChessBoard():
    t.speed(0)
    t.pencolor("black")
    #横线
    for i in range(num):
        t.forward(num * long)
        t.penup()
        t.goto(0, -long * (i + 1))
        t.pendown()
    t.forward(num * long)
    #home
    t.penup()
    t.home()
    t.right(90)
    t.pendown()

    #竖线
    for i in range(num):
        t.forward(num * long)
        t.penup()
        t.goto(long * (i + 1), 0)
        t.pendown()
    t.forward(num * long)

def drawBall(x, y):
    tBall.clear()
    #产生随机坐标
    x_r = randint(0, num - 1)
    y_r = randint(0, num - 1)
    tBall.speed(0)
    tBall.fillcolor("cyan")
    if (x / long - x_r) > 0 \
        and (x / long - x_r) < 1 \
            and (y / -long - y_r) > 0 \
                and (y / -long - y_r) < 1:
        tBall.fillcolor("red")
    tBall.begin_fill()
    tBall.penup()
    tBall.goto(50 + x_r * long, -75 - y_r * long)
    tBall.pendown()
    tBall.circle(25)
    tBall.end_fill()

def draw():
    drawChessBoard()
    s = Screen()
    s.onscreenclick(drawBall)
    s.mainloop()
    done()

if __name__ == '__main__':
    draw()