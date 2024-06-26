# import colorgram
import turtle as turtle_module
import random
turtle_module.colormode(255)
t = turtle_module.Turtle()
t.speed("fastest")

#
#
# rgb_colors = []
# colors = colorgram.extract("colorpallete.jpg", 32)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_counts = 100
for dot_counts in range(1, num_counts + 1):
    t.dot(15, random.choice(color_list))
    # t.penup()
    t.forward(50)
    # t.penup()

    if dot_counts % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()