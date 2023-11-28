print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price=0
if size=="S" or size=="s":
    price+=15
elif size=="M" or size=="m":
    price+=20
elif size=="L" or size=="l":
    price+=25
else:
    print("Please enter the correct pizza size")

if add_pepperoni=="Y" or add_pepperoni=="y":
    if size=="S" or size=="s":
        price += 2
    elif size=="M" or size=="m":
        price += 3
    elif size=="L" or size=="l":
        price += 3
elif add_pepperoni=="N" or add_pepperoni=="n":
    price+=0
else:
    print("Please try again")

if extra_cheese=="Y" or extra_cheese=="y":
    price+=1
elif extra_cheese=="N" or extra_cheese=="n":
    price+=0
else:
    print("Please try again")
print(f"Total price is ${price}")

# OR

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill=0
# if size=="S":
#     bill=15
# elif size=="M":
#     bill=20
# elif size=="L":
#     bill=25
# if add_pepperoni=="Y":
#     if size == "S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
# print(f"Your final bill is: ${bill}.")

