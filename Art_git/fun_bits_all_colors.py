import discord
import time
import os
import tkinter as tk
from PIL import ImageGrab
import turtle
import random
my_secret = os.environ['token']

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
def r(): return random.randint(0, 255)


# print('#%02X%02X%02X' % (r(),r(),r()))
ollie = turtle.RawTurtle(canvas)
canvas.configure(bg="black")
ollie.speed(0)
ollie.pensize(1)
rtimes = random.randint(2, 4)

client = discord.Client()
#Token = "Put your Bot token in here"
channel_code = 948709747190796319


@client.event
# This sets up the bot and checks your file path for the screen shots
async def on_ready():
    print("Logged in")
    screenshots = 1

    def dump_gui():
        print('...dumping gui window to png')

        x0 = root.winfo_rootx()
        y0 = root.winfo_rooty()
        x1 = x0 + root.winfo_width()
        y1 = y0 + root.winfo_height()
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(r"\bot_art" + str(screenshots) + ".png")
    while screenshots < 10000:
        for i in range(rtimes):
            # random.shuffle(colors)
            rsides = random.randint(3, 10)
            rangles = random.randint(5, 20)
            rtimes2 = random.randint(15, 45)
            rlenght = random.randint(50, 200)
            # ollie.forward(rsides)
            # ollie.left(rtimes2)
            for _ in range(3):
                # print(i)
                ollie.pencolor('#%02X%02X%02X' % (r(), r(), r()))
                ollie.left(rangles)
                for i in range(rtimes2):
                    ollie.left(360/rtimes2)
                    for i in range(rsides):
                        ollie.forward(rlenght)
                        ollie.right(360/rsides)

        dump_gui()
        print("trying to upload file numer " + str(screenshots))
        try:
            # put your channel code here
            channel = client.get_channel(channel_code)

            await channel.send(file=discord.File(r"\bot_art" + str(screenshots) + ".png"))
            print("succesfully uploaded")
            screenshots += 1

        except:
            time.sleep(10)
            print("Failed waiting 5 seconds for another")
        ollie.clear()

        print(screenshots)
client.run(my_secret)
