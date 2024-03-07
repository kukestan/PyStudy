from tkinter import * # type:ignore
from random import * # type:ignore
window = Tk()
window.title("canvas")
c = Canvas(window, height = 400, width = 400)
c.pack()
length = 100
for y in range(0, 4):
    for x in range(0, 4):
        Xor = x * length
        Yor = y * length
        c.create_rectangle(Xor, Yor, Xor + length, Yor + length, fill = 'darkblue')

Xor = randint(2, 3) * length
Yor = randint(2, 3) * length
island = c.create_rectangle(Xor, Yor, Xor + length, Yor + length, fill = 'green')
c.move(island, 0, 50)
window.mainloop()