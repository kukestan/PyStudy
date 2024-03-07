import turtle
import public.log as log
"""
太极图案
"""
color1="cyan"
color2="blue"

def draw():
    log.logd("画太极图案")
    turtle.speed(2)

    turtle.fillcolor(color1)
    turtle.begin_fill()
    turtle.circle(100, 180)
    turtle.end_fill()

    turtle.fillcolor(color2)
    turtle.begin_fill()
    turtle.circle(100, 180)
    turtle.end_fill()

    turtle.fillcolor(color2)
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.end_fill()

    turtle.right(180)

    turtle.fillcolor(color1)
    turtle.begin_fill()
    turtle.circle(50, -180)
    turtle.end_fill()

    turtle.up()
    turtle.goto(0, 150)
    turtle.down()

    turtle.fillcolor(color2)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.up()
    turtle.goto(0, 50)
    turtle.down()

    turtle.fillcolor(color1)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.done()

if __name__ == '__main__':
    draw()