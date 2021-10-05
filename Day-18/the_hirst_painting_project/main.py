import turtle as t
import random as rd

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.up()
tim.ht()

color_list = [(58, 106, 148), (225, 200, 109), (133, 84, 58), (224, 138, 61), (196, 145, 171), (234, 227, 205),
              (141, 178, 204), (140, 81, 104), (209, 90, 69), (238, 225, 234), (189, 79, 119), (135, 182, 137),
              (68, 105, 90), (136, 134, 72), (61, 156, 94), (46, 156, 193), (183, 192, 201), (215, 176, 192),
              (19, 58, 93), (21, 67, 113), (111, 123, 151), (229, 174, 165), (172, 203, 181), (69, 58, 47),
              (158, 205, 216), (114, 45, 58), (48, 75, 70), (72, 64, 51)]

tim.seth(225)
tim.forward(300)
tim.seth(0)
num_of_dots = 100
# def draw_and_move(moving_time, pixel_size):
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, rd.choice(color_list))
    # tim.up()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.seth(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)


screen = t.Screen()
screen.exitonclick()