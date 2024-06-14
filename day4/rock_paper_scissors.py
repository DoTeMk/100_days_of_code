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

list_movements = [rock, paper, scissors]
user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
if 0 <= user_choice <=2:
    print(list_movements[user_choice])
    computer_choice = random.randint(0, (len(list_movements) - 1))
    print(f"Computer chose:\n {list_movements[computer_choice]}")

    if (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
        print("You won!")
    elif (user_choice == 2 and computer_choice == 0) or (user_choice < computer_choice):
        print("You lose!")
    elif user_choice == computer_choice:
        print("Drawn")
else:
    print("Invalid Option!")

    # 0 1 = win
    # 0 2 = lose
    
    # 1 0 = win
    # 1 2 = lose 

    # 2 0 = win 
    # 2 1 = lose 
    
    # win = 0 2 // 1 0 // 2 1 -------> win when user > computer, except in 0 2
    # lose = 0 1 // 1 2 // 2 0  ------> lose when user < computer, ecept in 2 0