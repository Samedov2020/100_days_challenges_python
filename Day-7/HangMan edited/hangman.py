import random
from hangman_words import word_list
from logo import logo
from stages import stages
print(logo)


# word_list = ["waterfall", "flametower", "hairdresser"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

lives=6

display = ["_" for _ in range(word_length)]


end_of_game = False
while not end_of_game:
    guess = input("write your guessed letter").lower()
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = guess
        # else:
        #     print("No Match!")
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")
    print(display)  # This line should be inside the while loop

    if "_" not in display:
        end_of_game = True
        print("You win")  # This line should be inside the while loop
    print(stages[lives])
