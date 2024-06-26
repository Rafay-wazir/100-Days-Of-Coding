# Calculator
# from replit import clear
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What's The First Number?: "))
    for symbol in operators:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick An Operation: ")
        num2 = float(input("What's The Next Number?: "))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(
                f"Type 'y' To Continue Calculating With {answer}, Or Type 'n' To Start A New Calculation: "
        ) == 'y':
            num1 = answer
            # if input(f"Type 'y' To Continue Calculating With {answer}, Or Type 'n' To Exit Or 's' To Start A New Calculation: ") == 'y':
        # elif 'n':
        #   should_continue = False
        #   print("Thank You For Using The Calculator")
        else:
            should_continue = False
            # clear()
            calculator()


calculator()
