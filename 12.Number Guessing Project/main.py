from art1 import logo
import random

print(logo)

print(r"""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
answer=random.randint(1,100)

easy_attempts=10
hard_attempts=5
Game_over=False
game_type=input("Choose a difficulty. Type 'easy' or 'hard':")
game_type=game_type.upper()

if game_type=="EASY":
    while not Game_over:
        print(f"you have {easy_attempts} remaining")
        guess = input("Make a Guess:")
        guess = int(guess)
        if guess == answer:
            print("You have found the correct number-->You Won!")
            Game_over = True
        else:
            easy_attempts = easy_attempts - 1
            if guess < answer:
                print("Too Low")
            if guess >answer:
                print("Too High")
            if easy_attempts==0:
                Game_over=True
                print(f"you have {easy_attempts} attempts remaining -->You Lose")

elif game_type=="HARD":
    while not Game_over:
        print(f"you have {hard_attempts} remaining")
        guess = input("Make a Guess:")
        guess = int(guess)
        if guess == answer:
            print("You have found the correct number-->You Won!")
            Game_over = True
        else:
            hard_attempts = hard_attempts - 1
            if guess < answer:
                print("Too Low")
            if guess >answer:
                print("Too High")
            if hard_attempts==0:
                Game_over=True
                print(f"you have {hard_attempts} attempts remaining -->You Lose")
else:
    print("Invalid_Game_Type")