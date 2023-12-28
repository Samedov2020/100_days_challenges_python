num=int(input("Check your number"))
if num > 1:
    for i in range(2,num):
        if i % num == 0:
            print(f"{num} is NOT a prime number")
            break
    else:
        print(f"{num} is a prime number")
elif num==0 or 1:
    print(f"{num} is neither prime nor composite number")
else:
    print(f"{num} is not a prime number.it is composite number.")