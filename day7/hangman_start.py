import random

word_list = ["aardvark", "baboon", "camel"]
display = []
chosen_word = random.choice(word_list)
game_over = False
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages) - 1

for _ in range(len(chosen_word)):
    display += "_"

while not game_over:     
    guess = input("Guess a letter in the word: ").lower()  
     
    for position in range(len(chosen_word)):
        c = chosen_word[position]
        if c == guess:
            display[position] = c        
    print(f"\n{' '.join(display)}\n")
    if "_" not in display:
        print("You Won!")
        game_over = True
    elif guess not in chosen_word:
        print(stages[lives])
        lives -= 1 
        if lives < 0:
            print("You lose!")
            game_over = True