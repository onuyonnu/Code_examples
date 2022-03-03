import turtle
import random
import requests
from bs4 import BeautifulSoup


response = requests.get('https://htmlcolorcodes.com/colors/').text
soup = BeautifulSoup(response, "lxml")
#Pulls a master list of colors from htmlcolorcodes.com
colors = []
for color in soup.find_all("td"):
    try:
        Hex = color.find("div", class_="color-table__color js-color")["data-hex"]
    except Exception as e:
        pass
    colors.append(Hex)
#turtle import setup the gui
wn = turtle.Screen()
wn.bgcolor("black")
ollie = turtle.Turtle()
ollie.speed(0)
ollie.pensize(1)
rtimes = random.randint(6, 10)
#randomizes the size shape and frequency of the patern
for i in range(rtimes):
    random.shuffle(colors)
    rsides = random.randint(3, 10)
    rangles = random.randint(15, 30)
    rtimes2 = random.randint(5, 30)
    rlenght = random.randint(50, 250)
    for i in colors[:2]:
        print(i)
        ollie.pencolor(i)
        ollie.left(rangles)
        for i in range(rtimes2):
            ollie.left(360/rtimes2)
            for i in range(rsides):
                ollie.forward(rlenght)
                ollie.right(360/rsides)
wn.exitonclick()
