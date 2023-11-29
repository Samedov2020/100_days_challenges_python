import random
names_string = input("Enter names separated by commas: ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_pays = names[random_choice]

print(person_who_pays + " is going to buy the meal today!")



# OR


# import random
#
# names_string = input("Enter your names: ")
# names_list = names_string.split(", ")
#
# count = len(names_list)
#
# if count >= 5:
#     random_number = random.randint(0, count - 1)
#     print(names_list[random_number])
# else:
#     print("Not enough names")
