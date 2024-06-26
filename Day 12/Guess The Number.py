from random import randint
from art import logo

EASY = 10
HARD = 5


# Checking The User's Guess Against The Acutal Answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You Got It! The Answer Was {answer}. ")


    # Setting The Difficulties
def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY
        elif level == "hard":
            return HARD
        else:
            print("Invalid Input, Please Try Again. ")


# Imporing Random Number And Welcomming The User
def game():
    print(logo)
    print("Welcome To The Number Guessing Game! ")
    print("I Am Thinking Of A Number Between 1 And 100")
    answer = randint(1, 100)
    # print(f"The Correct answer Is {answer}")

    #  Setting The Function To Repeat If They Go Wrong
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You Have {turns} Attempts To Guess The Number")
        # Letting The User Make A guess
        guess = int(input("Make A Guess: "))
        # Track The Number Of Turns And Reduces By 1 If They Get It Wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've Run Out Of Guesses, You Lose")
            print(f"The Correct Answer Was {answer}")
            return
        elif guess != answer:
            print("Guess Again")


game()
