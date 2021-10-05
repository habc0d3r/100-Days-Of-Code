# import turtle
# timmy = turtle.Turtle()
# timmy is an object, turtle is the module
# and Turtle() is the class. We are tapping into the Turtle class
# which is declared in the turtle module and constructing an
# object called timmy using () with class
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle"), timmy.color('DarkOrchid1')
# for i in range(3):
#     timmy.forward(100), timmy.left(120)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Sl. no.', [1, 2, 3])
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
# print(table.align)
table.align = 'l'

print(table)
