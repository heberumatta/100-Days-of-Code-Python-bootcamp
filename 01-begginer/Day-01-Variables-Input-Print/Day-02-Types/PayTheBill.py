print("Welcome to the tip calculator by Heber!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? %"))
people = int(input("How many people to split the bill? "))

bill = round(((((tip/100) + 1)*bill)/people),2)

print(f"Each person should pay: ${bill}")
