from tkinter import * # type:ignore

def eye_control(event):
    key = event.keysym
    if key == 'Up':
        c.move(eyeball, 0, -5)
        c.itemconfig(words, text = '上')
    elif key == 'Down':
        c.move(eyeball, 0, 5)
        c.itemconfig(words, text = '下')
    elif key == 'Left':
        c.move(eyeball, -5, 0)
        c.itemconfig(words, text = '左')
    elif key == 'Right':
        c.move(eyeball, 5, 0)
        c.itemconfig(words, text = '右')
    elif key == 'b':
        c.moveto(eyeball, 190, 90)
        c.itemconfig(words, text = '眼睛回来了')


window = Tk()
window.title("Alien")
c = Canvas(window, height = 300, width = 400)
c.pack()
body = c.create_oval(100, 150, 300, 250, fill = 'green')
eye = c.create_oval(170, 70, 230, 130, fill = 'white')
eyeball = c.create_oval(190, 90, 210, 110, fill = 'black')
mouth = c.create_oval(150, 220, 250, 240, fill = 'red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill = 'blue')
words = c.create_text(300, 120, text = "")
c.bind_all('<Key>', eye_control)
window.mainloop()