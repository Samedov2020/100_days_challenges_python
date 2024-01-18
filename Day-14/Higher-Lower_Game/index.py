from art import logo ,vs
from game_data import data
from replit import clear
import random

def format_data(account):
    """Format the account data into printable format."""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name} , a {account_descr}, from {account_country}"

def check_answer(guess,a_follower,b_follower):
    """Guess the user guess and follower count if they got it right """
    if a_follower>b_follower:
        return guess=="a"
    else:
        return guess=="b"
#Display Art
print(logo)
score=0
game_should_continue=True
account_b =random.choice(data)


while game_should_continue:
        #Generate a random account from the game data 
        account_a= account_b
        accunt_b=random.choice(data)
        if account_a==account_b:
            account_b=random.choice(data)
            
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
        
        guess=input("Who has mor followers? 'A' or 'B' : ").lower()
        
        #check if user is right
        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        is_correct=check_answer(guess, a_follower_count, b_follower_count)
        clear()
        if is_correct:
            score+=1
            print(f"You are right , Current score is {score}")
        else:
            game_should_continue=False
            print(f"Sorry that is wrong! Final score is {score}")

