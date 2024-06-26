from turtle import Turtle, Screen

julia = Turtle()
print(julia)
julia.shape("turtle")
julia.color("red", "blue")

# def move_turtle():
#     julia.forward(100)
#     julia.back(100)
for _ in range(5):
    # julia.speed(5)
    # julia.fillcolor("yellow")
    julia.forward(100)
    julia.right(90)
    julia.back(100)
    julia.right(90)
    julia.forward(100)
    julia.left(90)
    julia.forward(100)
    julia.left(90)
    # move_turtle()

my_screen = Screen()
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = ("l")
print(table)