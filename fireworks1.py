import turtle
import random


turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(0)


def pen_colour(color):
    t.color(color)


def fireworks(distance):
    for _ in range(20):
        t.forward(distance)
        t.right(180 - (360 / 20))


def move():
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()


colors = ['red', 'purple', 'green', "orange", "yellow", "cyan"]


for _ in range(30):
    pen_colour(random.choice(colors))
    fireworks(random.randint(50, 100))
    move()

turtle.done()

