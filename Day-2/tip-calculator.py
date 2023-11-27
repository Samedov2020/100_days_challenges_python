
print("Welcome to the Tip calculator")
total_bil=float(input("What was the total bill? "))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12 or 15 "))
split=int(input("How many people to split the bill? "))
eachperson_pays=float((total_bil+(total_bil * tip_percentage)/100)/split)
print(f"Each person should pay: ${round(eachperson_pays ,2)}")



# print("Welcome to the tip calculator.")
# bill=input("What was the total bill? ")
# tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
# split=input("How many people to split the bill? ")
# bill_as_float=float(bill)
# tip_as_int=int(tip)
# split_as_int=int(split)
# pay=(bill_as_float+bill_as_float*tip_as_int/100)/split_as_int
# print(f"Each person should pay: {round(pay,2)}")