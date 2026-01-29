import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def fireworks(distance):
    for _ in range(20):
        t.forward(distance)
        t.right(180 - (360 / 20))

def move():
    t.penup()
    t.goto(random.randint(-300,300), random.randint(-300,300))
    t.pendown()

colors = ['red', 'purple', 'green', 'orange', 'yellow', 'cyan']

for _ in range(30):
    t.color(random.choice(colors))
    fireworks(random.randint(50, 100))
    move()

turtle.exitonclick()

