print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm\n"))

if height < 0:
    print("Input correct number")
elif 0 <= height < 120:
    print("Sorry, you have to grow taller before you can ride")
elif height >= 120:
    age = int(input("Input your age:\n"))
    if age < 12:
        bill=5
        print("Child tickets are 5$")
    elif 12 <= age <= 18:
        bill=7
        print("Youth tickets are 7$")
    else:
        bill=12
        print("Adult tickets are 12$")

    photo=input("Do you want a photo taken? Y or N ")
    if photo=="Y":
        bill=bill+3
    print(f"Your final bill is {bill}")




# OR

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm\n"))
#
# if height < 0:
#     print("Input correct number")
# elif 0 <= height < 120:
#     print("Sorry, you have to grow taller before you can ride")
# elif height >= 120:
#     picture=input("Do you want a photo taken? Yes or No")
#     if picture=="Yes" or picture=="yes":
#         age = int(input("Input your age:\n"))
#         if age < 12:
#             print("Child tickets are 8$")
#         elif 12 <= age <= 18:
#             print("Youth tickets are 10$")
#         else:
#             print("Adult tickets are 15$")
#     else :
#         age = int(input("Input your age:\n"))
#         if age < 12:
#             print("Child tickets are 5$")
#         elif 12 <= age <= 18:
#             print("Youth tickets are 7$")
#         else:
#             print("Adult tickets are 12$")
#
