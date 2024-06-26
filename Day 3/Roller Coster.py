print("Welcome To The Rollarcoster Ride!")
height = int(input("What's Your Height In Cm? "))
bill = 0
if height >= 120:
  print("You Can Ride The Rollarcoster!")
  age = int(input("What's Your Age? "))
  if age < 12:
    bill = 5
    print("Child Tickets Are $5.")
  elif age < 18:
    bill = 7
    print("Youth Tickets Are $7.")
  elif age >= 45 and age <= 55:
    print("Everything Is Going To Be Ok. Have A Free Ride On Us!")
  else:
    bill = 12
    print("Adult Tickets Are $12.")

  wants_a_photo = input("Do You Want Photo? Y or N ").upper()
  if wants_a_photo == "Y":
    bill += 3

  print(f"Your Final Bill Is ${bill}")
else:
  print("Sorry You Can't Ride The Rollarcoster")
