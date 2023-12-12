word_list=["umbrella","waterfall","hairdresser"]
import random
random_choice=random.choice(word_list)
guess=input("Guess the letter of the word").lower()
for letter in random_choice:
    if letter==guess:
        print("Right!")
    else:
        print("Wrong! Try again!")