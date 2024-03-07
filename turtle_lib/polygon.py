import turtle

"""
绘制正多边形
"""
def paint(n, long):
    for i in range(n):
        turtle.forward(long)
        turtle.right(180 - (n - 2) * 180 / n)

def draw():
    turtle.speed(1)
    turtle.fillcolor("green")
    #开始涂色
    turtle.begin_fill()
    for i in range(3, 11):
        paint(i, 50)
    #结束涂色
    turtle.end_fill()
    turtle.done()

if __name__ == '__main__':
    draw()
