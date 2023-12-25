import random
word_list = ["waterfall", "flametower", "hairdresser"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

display = ["_" for _ in range(word_length)]
print(display)

end_of_game = False
while not end_of_game:
    guess = input("write your guessed letter").lower()
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)  # This line should be inside the while loop

    if "_" not in display:
        end_of_game = True
        print("You win")  # This line should be inside the while loop
