import turtle
import time
from pygame import mixer


mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("hbd-song.mp3") # add your music file name or path


# sets background
bg = turtle.Screen()
bg.title("Wish him a hapy bday") # Change to whatever you want
bg.bgcolor("black")
mixer.music.play()


# Bottom Line 1
turtle.penup()
turtle.goto(-100,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-100,-160)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-100,-135)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("black")

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("azure")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("black")


# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("black")


# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("black")

# Happy Birthday message

turtle.penup()
turtle.goto(-250, 50)
turtle.color("pink")
turtle.pendown()


turtle.write(arg=f" ???? ", align="left", font=("jokerman", 15, "normal")) # Change the display message

time.sleep(5)
