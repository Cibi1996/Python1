print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island \n Your mission is to find the treasure")
print("You're at a cross road. Where do you want to go?")
answer=input('''Type "Right" or "Left"''')
answer1=answer.lower()
answer2=""
answer3=""
answer4=""
answer5=""

if answer1 == "left":
    answer2=input('''You've come to a lake. There is an island in the middle of the lake.\n
    Type "wait" to wait for a boat. Type "swim" to swim across.''')
    answer3=answer2.lower()


    if answer3 == "wait":
        answer4 = input('''You arrive at the island unharmed. There is a house with 3 doors.
      One red, one yellow and one blue. Which colour do you choose?''')
        answer5 = answer4.lower()
        if answer5 == "red":
            print("Burned by fire.\nGame Over.")
        elif answer5 == "yellow":
            print("You find the Treasure! You Win!")
        elif answer5 == "blue":
            print("Eaten by beast\n Game over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\n Game Over")

else:
    print("You fell into a hole. Game Over.")






