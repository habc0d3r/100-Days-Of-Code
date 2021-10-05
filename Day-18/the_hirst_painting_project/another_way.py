import turtle as t
import random as rd

t.colormode(255)

tim = t.Turtle()
tim.speed(0)
tim.up()
tim.hideturtle()
tim.setpos(-220, -210)


color_list = [(58, 106, 148), (225, 200, 109), (133, 84, 58), (224, 138, 61), (196, 145, 171), (234, 227, 205),
              (141, 178, 204), (140, 81, 104), (209, 90, 69), (238, 225, 234), (189, 79, 119), (135, 182, 137),
              (68, 105, 90), (136, 134, 72), (61, 156, 94), (46, 156, 193), (183, 192, 201), (215, 176, 192),
              (19, 58, 93), (21, 67, 113), (111, 123, 151), (229, 174, 165), (172, 203, 181), (69, 58, 47),
              (158, 205, 216), (114, 45, 58), (48, 75, 70), (72, 64, 51)]

def draw_and_move(moving_time):
    for _ in range(moving_time - 1):
        tim.dot(20, rd.choice(color_list))
        tim.forward(50)


def move_left(moving_time, angle):
    tim.left(angle)
    draw_and_move(moving_time)
    tim.left(angle)


def move_right(moving_time, angle):
    tim.right(angle)
    draw_and_move(moving_time)
    tim.right(angle)


for _ in range(5):
    draw_and_move(10)
    move_left(2, 90)
    draw_and_move(10)
    move_right(2, 90)

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
screen = t.Screen()
screen.exitonclick()


