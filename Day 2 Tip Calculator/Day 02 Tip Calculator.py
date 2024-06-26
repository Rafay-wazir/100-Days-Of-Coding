print("Welcome To Tip Calculator")
bill = float(input("What is The Total Bill $ "))
split = int(input("How Many To Split The Bill? "))
tip = int(input("What Percentage Would You Like To Do? 10, 12, 15? "))

total_bill = bill * (1 + tip / 100 )
final_bill = round(total_bill / split, 2)
print(f"Each Person Should Pay ${final_bill}")

