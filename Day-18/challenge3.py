from turtle import Turtle, Screen
import random as rd

colors = ['chartreuse', 'deep sky blue', 'sandy brown', 'medium orchid', 'magenta', 'royal blue', 'burlywood']

tim = Turtle()
tim.shape("arrow")


def change_color():
    tim.color(rd.random(), rd.random(), rd.random())


def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)
        change_color()
        # tim.color(rd.choice(colors))

for side in range(3, 11):
    draw_shape(side)

screen = Screen()
screen.exitonclick()
