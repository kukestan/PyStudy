import turtle

s = turtle.Screen()

def semi(n):
    turtle.circle(20 * n, 180)

def draw():
    turtle.speed(5)
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(1, 11):
        semi(i)
    turtle.end_fill()
    turtle.done()

if __name__ == '__main__':
    draw()