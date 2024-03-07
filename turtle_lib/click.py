import turtle

"""
点击画圆
"""
s = turtle.Screen()

def draw_circle(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor((0, 0.1, 0.1))
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

def draw():
    turtle.speed(0)
    s.onscreenclick(draw_circle)
    s.mainloop()

if __name__ == '__main__':
    draw()