# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilogams: "))
bmi=float(weight/height**2)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5<=bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25<=bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30<=bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi>=35:
    print(f"Your BMI is {bmi}, you are clinically obese.")