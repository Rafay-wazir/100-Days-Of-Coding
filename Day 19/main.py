from turtle import Turtle, Screen
import random
screen = Screen()
is_bet_chosen = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle Will Win The Race? Enter A Color: ")
colors = ["red", "yellow", "blue", "green", "magenta"]
positions = [100, 50, 0, -50, -100]
all_turtle = []

for turtle_index in range(0, 5):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[turtle_index])
    new_t.penup()
    new_t.goto(x=-230, y=positions[turtle_index])
    all_turtle.append(new_t)

if user_bet:
    is_bet_chosen = True

while is_bet_chosen:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_bet_chosen = False
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} Turtle Is The Winner. ")
            else:
                print(f"You've lost! The {winning_color} Turtle Is The Winner. ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()


# tom.speed("slow")

# def move_forward():
#     t.forward(20)
#     tom.backward(20)

# def move_backwards():
#     t.backward(20)
#     tom.forward(20)

# def move_clockwise():
#     add_heading = t.heading() + 10
#     tom_heading = tom.heading() - 10
#     t.setheading(add_heading)
#     tom.setheading(tom_heading)

# def move_anticlockwise():
#     minus_heading = t.heading() - 10
#     tom_minus = tom.heading() + 10
#     t.setheading(minus_heading)
#     tom.setheading(tom_minus)
#
# def clear_screen():
#     t.clear()
#     tom.clear()
#     t.penup()
#     tom.penup()
#     t.home()
#     tom.home()
#     t.pendown()
#     tom.pendown()
#
# screen.onkey(move_backwards, "s")
# screen.onkey(move_forward, "w")
# screen.onkey(move_clockwise, "a")
# screen.onkey(move_anticlockwise, "d")
# screen.onkey(clear_screen, "c")

# screen.onkey(key="space", fun=move_forward)








