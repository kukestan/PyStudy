from turtle import *

def draw():
    speed(0)
    screensize(bg="green")
    for i in range(12):
        circle(100)
        right(30)
    done()

if __name__ == '__main__':
    draw()