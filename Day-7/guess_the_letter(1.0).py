word_list=["umbrella","waterfall","hairdresser"]
import random
random_choice=random.choice(word_list)
guessed_list=[]
word_length=len(random_choice)
for _ in range(word_length):
    guessed_list+="_"
print(guessed_list)
    
guess=input("Guess the letter of the word").lower()

for position in range(word_length):
    letter=random_choice[position]
    if letter==guess:
        guessed_list[position]=letter
print(guessed_list)
    



