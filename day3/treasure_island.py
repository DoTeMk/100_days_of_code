print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You've encountered 2 paths during your exploration inside the cave. Wich path are you going to choose?" 
                "Type 'left' or 'right'\n").lower()
if choice1 == 'left':
    choice2 = input("You find your way out of the cave. Now there's a lake in your front and you see a small island in the middle. "
                    "Type 'wait' to wait for a boat or type 'swin' to swin across.\n").lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There's a old boat and you can see 3 different crates on deck: one yellow, one red and one blue."
                        "Wich colour you choose to open?\n").lower()
        if choice3 == 'yellow':
            print("You win!")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("You become frozen. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Attacked by Kraken. Game Over.")
else:
    print("Fall into a hole. Game Over.")