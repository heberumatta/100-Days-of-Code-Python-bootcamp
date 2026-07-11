height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight: "))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height ** 2))

print(f"Your BMI is: {bmi:.2f}kg/m")
