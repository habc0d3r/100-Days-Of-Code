import turtle
from turtle import Turtle, Screen
import random as rd

tim = Turtle()
# tim.hideturtle()
turtle.colormode(255)


def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    final_color = (r, g, b)
    return final_color


directions = [0, 90, 180, 270]
tim.speed(0)
tim.pensize(10)
for _ in range(200):
    tim.color(random_color())
    tim.fd(20)
    tim.seth(rd.choice(directions))

screen = Screen()
screen.exitonclick()
