import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]


mychoice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
mychoice=int(mychoice)


if mychoice >=3 or mychoice<0:
    print("Invalid option. Game over")

else:

    print(game_images[mychoice])



    computerchoice = random.randint(0, 2)
    print("computer choose")
    print(game_images[computerchoice])


    if mychoice==0 and computerchoice==0:
        print("Draw")
    elif mychoice==0 and computerchoice==1:
        print("You lose")
    elif mychoice==0 and computerchoice==2:
        print("You win")
    elif mychoice==1 and computerchoice==0:
        print("You Win")
    elif mychoice==1 and computerchoice==1:
        print("Draw")
    elif mychoice==1 and computerchoice==2:
        print("You lose")
    elif mychoice==2 and computerchoice==0:
        print("You Lose")
    elif mychoice==2 and computerchoice==1:
        print("You win")
    elif mychoice==2 and computerchoice==2:
        print("Draw")


