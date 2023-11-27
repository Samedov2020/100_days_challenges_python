#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
age = input("Enter your age\n")
max_limit=4680
age_to_int=int(age)
weeks_til_today=age_to_int*52
weeks_left=max_limit - weeks_til_today
print(f"You have {weeks_left} weeks left.")
