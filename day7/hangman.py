# creating a hangman using python
# request all the modules for the application

import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

# function to clear the console


def clear():
    os.system('clear')


print(logo)
# check if the game is finished or not.
game_is_finished = False
lives = len(stages) - 1

# choice an random word using the module
chosen_word = random.choice(word_list)
# get the length of that word
word_length = len(chosen_word)

# create an dic to add the word in form of spaces [ _ _ _ _]
display = []

# loop the array to create the spaces based on the word that it was chosen
for _ in range(word_length):
    display += "_"
# goes into a loop to check if the game finished or not using while loop
while not game_is_finished:
    guess = input("Guess the letter: ").lower()
    # Using the clear function to make the UX better
    clear()
    if guess in display:
        print(f"You already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # check if the letter isn't inisde the chosen word
    if guess not in chosen_word:
        print(f"You guessed  {guess}, thats not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    # Check if the spaces inside the word is all filled in
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
