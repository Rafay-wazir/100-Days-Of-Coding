import random
computer_choice = random.randint(0,2)
person_choice = int(input("What Do You Choose? Type 0 For Rock, 1 For Paper And 2 For Scissors.\n"))
print(f"Computer Chose {computer_choice}")
if person_choice >= 3 or person_choice < 0:
  print("You Typed An Invalid Number, You Lose!")
elif person_choice == 0 and computer_choice == 2:
  print("You Win!")
elif computer_choice == 0 and person_choice == 2:
  print("You Lose.")
elif person_choice == 1 and computer_choice == 0:
  print("You win!")
elif person_choice == 2 and computer_choice == 1:
  print("You Win!")
elif person_choice == computer_choice:
  print("Tie Game.")
elif computer_choice > person_choice:
  print("You Lose.")