import turtle

def draw():
    t = turtle.Pen()
    #设置填充颜色
    t.fillcolor("red")
    #开始填充
    t.begin_fill()
    for i in range(5):
        #向前移动300
        t.forward(300)  
        t.right(180-180/5)   #180-五角星的内角和/5
        #结束填充
        t.end_fill()
    turtle.done()

if __name__ == '__main__':
    draw()