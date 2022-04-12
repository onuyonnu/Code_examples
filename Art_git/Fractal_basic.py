import turtle
import random
import tkinter as tk
from PIL import ImageGrab


def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    ImageGrab.grab().crop(
        (x0, y0, x1, y1)).save(r"D:\art_dump\test" + str(screenshots) + ".png")


# Setup of all the randomizing functions for shapes and colors aswell as ui
root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()
r_rgb = lambda: random.randint(0, 255)
rsides = lambda: random.randint(3, 10)
rangles = lambda: random.randint(5, 20)
rocelation = lambda: random.randint(15, 45)
rlenght = lambda: random.randint(50, 250)
ollie = turtle.RawTurtle(canvas)
canvas.configure(bg="black")
ollie.speed(0)
ollie.pensize(1)
rtimes = lambda: random.randint(3, 5)
screenshots = 1


def sort_key(shape):
    return (shape[1] * shape[4])


while screenshots < 10:
    shapes = []
    for i in range(rtimes()):
      #random.shuffle  0       1          2           3            #4
        newshape = (int(i), rsides(), rangles(), rocelation(), rlenght())
        
        shapes.append(newshape)
      #This sorts the shapes created so as to make it so the largest shapes are drawn first
    shapes.sort(key=sort_key, reverse=True)
    for i in shapes:
        Cshape = i
        print(f"curent shape, sides {Cshape[1]}, angle {Cshape[2]}, ocelation {Cshape[3]}, length {Cshape[4]} ")
        
        for _ in range(3):
            ollie.pencolor('#%02X%02X%02X' % (r_rgb(), r_rgb(), r_rgb()))
            #angles
            ollie.left(Cshape[2])
            #ocelation
            for i in range(Cshape[3]):
                ollie.left(360 / Cshape[3])
                #sides
                for i in range(Cshape[1]):
                    #length
                    ollie.forward(Cshape[4])
                    #sides
                    ollie.right(360 / Cshape[1])

    dump_gui()
    screenshots += 1
    ollie.clear()
print("Done making art going to sleep now")
