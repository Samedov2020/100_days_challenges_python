print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm\n"))
if height<0 :
    print("Input correct number")
elif height<120 and height>=0:
    print("Sorry, you have to grow taller before you can ride")
elif height>=120:
    print("You can rithe the rollercoaster!")
    age=int(input("Input your age:\n"))
    if age<18:
        print("Ticket price is 7$")
    else :
        print("Ticket price is 12$")

