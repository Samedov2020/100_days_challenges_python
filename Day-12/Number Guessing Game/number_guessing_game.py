from random import randint
from art import logo

easy_level_turns=10
hard_level_turns=5

def check_answer(answer,guess,turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it.Answer was {answer}")
        
        
def set_difficulty():
    level=input("Choose a difficulty.Type 'Easy' or 'Hard' ").lower()
    if level=='easy':
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking if a number between 1 and 100")
    answer=randint(1, 100)
    print(f"The correct answer is {answer}")
    
    turns = set_difficulty()
    
    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess=int(input("Make a guess: "))
        turns=check_answer(answer, guess,turns)
        if turns==0:
            print("You have run out of guesses , You lose!")
            return
        elif guess !=answer:
            print("Guess again!")
game()
