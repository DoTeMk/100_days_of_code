import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
game_over = False
lives = len(stages) - 1
guessed_letters = []

print(logo)

display = []
for _ in range(len(chosen_word)):
    display += "_"

while not game_over: 
    guess = input("Guess a letter in the word: ").lower() 
    
    if guess in guessed_letters:
        print(f"You've already tried {guess}. Try another one.")
    else:
        for position in range(len(chosen_word)):
            c = chosen_word[position]
            if c == guess:
                display[position] = c
            else:
                guessed_letters.append(guess) 

        print(f"\n{' '.join(display)}\n")

        if "_" not in display:
            print("You Won!")
            game_over = True

        elif guess not in chosen_word:
            print(f"The {guess} is not in the word. You lose 1 life.")
            print(stages[lives])
            lives -= 1 
            if lives < 0:
                print("You lose!")
                game_over = True