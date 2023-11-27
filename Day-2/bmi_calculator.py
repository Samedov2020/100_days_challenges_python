# 1st input: enter height in meters e.g: 1.65
height = input("Write your height\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Write your height\n")

height_to_float=float(height)
weight_to_int=int(weight)
BMI=int(weight_to_int / (height_to_float **2))
print(BMI)