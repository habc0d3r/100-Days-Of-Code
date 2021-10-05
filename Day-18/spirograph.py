import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


tim.speed("fastest")

# for _ in range(75):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.settiltangle(5)
#     tim.left(5)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
