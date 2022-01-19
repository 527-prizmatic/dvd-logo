from tkinter import *
from PIL import ImageTk, Image
import time
import random

def movemake():
    global mx; mx = 1
    global my; my = 1

def moveimg(event=None):
    global mx
    global my
    global ix
    global iy
    c.move(i, mx, my)
    ix += mx
    iy += my
    if ix > cx-20 or ix < 20:
        mx = -mx
        chghue()
    if iy > cy-20 or iy < 20:
        my = -my
        chghue()
    c.after(25, moveimg)

def chghue():
    global img
    global i
    global h; h += 1
    if h >= 6: h -= 6
    for y in range(img.height()):
        for x in range(img.width()):
            if img.transparency_get(x, y) == False:
                if h == 0: img.put('#%02x%02x%02x' % (255, 0, 0), (x, y))
                elif h == 1: img.put('#%02x%02x%02x' % (255, 255, 0), (x, y))
                elif h == 2: img.put('#%02x%02x%02x' % (0, 255, 0), (x, y))
                elif h == 3: img.put('#%02x%02x%02x' % (0, 255, 255), (x, y))
                elif h == 4: img.put('#%02x%02x%02x' % (0, 0, 255), (x, y))
                elif h == 5: img.put('#%02x%02x%02x' % (255, 0, 255), (x, y))
    c.delete(i)
    i = c.create_image(ix, iy, image=img)

window = Tk()
window.title("DVD")
window.configure(bg='black')
cx = 320
cy = 180
ix = random.randint(20, cx-20)
iy = random.randint(20, cy-20)
c = Canvas(window, bg='black', width=cx, height=cy)
c.pack(expand=1, fill=BOTH)
img = PhotoImage(file = "data/dvd.png")
i = c.create_image(ix, iy, image=img)
h = 0;
movemake()
c.bind('<Expose>', moveimg)

window.mainloop()