from turtle import Turtle, Screen
# from turtle import *  <<< avoid importing this way
# alias modules
# import turtle as t
# import random as rd
# print(rd.choice([1, 3, 6]))
tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
