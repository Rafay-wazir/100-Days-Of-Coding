print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write_ your code below this line 👇
choice_1 = input(
    'You Are At Crossroad, Where You Want To Go? Type "left" or "right" \n '
).lower()

if choice_1 == "left":
    choice_2 = input(
        'You Have Come To A Lake. There Is An Island In The Middle Of The Lake. Type "Wait"To Wait For A Boat. Type "Swim" To Swim Across \n'
    ).lower()
    if choice_2 == "wait":
        choice_3 = input(
            "You Have Arrived At The Island Unharmed. There Is A House With 3 Doors. One Red, One Yellow And One Blue. Which Colour Do You Choose? \n"
        ).lower()
        if choice_3 == "red":
            print("It's A Room Full Of Fire. Game Over.")
        elif choice_3 == "yellow":
            print("It's A Room Full Of Beasts. Game Over.")
        elif choice_3 == "blue":
            print("It's A Room Full Of Treasure. You Win!")
        else:
            print("You Choose A Door That Doesn't Exist. Game Over.")
    else:
        print("You Got Attacked By An Angry Trout. Game Over.")

else:
    print("You Fell Into A Hole. Game Over.")
