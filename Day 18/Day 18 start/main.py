# import turtle as t   # alias name (t) given by us
import turtle
from turtle import Turtle, Screen
import random

# rainbow = t
turtle.colormode(255)
rainbow = Turtle()

# import heroes
#
# print(heroes.gen())


# rainbow.shape("turtle")

# for _ in range(15):
#     # rainbow.forward(10)
#     # rainbow.color("white")
#     # rainbow.forward(10)
#     # rainbow.color("black")
#     rainbow.forward(10)
#     rainbow.penup()
#     rainbow.forward(10)
#     rainbow.pendown()

# for _ in range(3):
#     rainbow.forward(100)
#     rainbow.right(360/3)
# for _ in range(4):
#     rainbow.forward(100)
#     rainbow.right(360/4)
# for _ in range(5):
#     rainbow.forward(100)
#     rainbow.right(360/5)
# for _ in range(6):
#     rainbow.forward(100)
#     rainbow.right(360/6)
# for _ in range(7):
#     rainbow.forward(100)
#     rainbow.right(360/7)
# for _ in range(8):
#     rainbow.forward(100)
#     rainbow.right(360/8)
# for _ in range(9):
#     rainbow.forward(100)
#     rainbow.right(360/9)
# for _ in range(11):
#     rainbow.forward(100)
#     rainbow.right(360/10)
#
# tinker_color = ["chartreuse", "light sky blue", "sienna", "chartreuse", "red", "light goldenrod yellow", "magenta",
#                 "yellow", "pink", "slate gray"]


# def draw_shapes(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         rainbow.forward(100)
#         rainbow.right(angle)


# for shape_sides in range(3, 11):
#     rainbow.color(random.choice(tinker_color))
#     draw_shapes(shape_sides)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
#
# directions = [0, 90, 180, 270]
# rainbow.pensize(5)


rainbow.speed("fastest")
#
# for _ in range(200):
#     rainbow.color(random_color())
#     rainbow.forward(40)
#     rainbow.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        rainbow.speed("fastest")
        rainbow.color(random_color())
        rainbow.circle(100)
        current = rainbow.heading()
        rainbow.setheading(current + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()

