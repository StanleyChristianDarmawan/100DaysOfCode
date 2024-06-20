import os
import random
import hangman_art
from hangman_words import word_list

clear = lambda: os.system('cls')
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
lives = 6

print(hangman_art.logo)

# print(f'The solution is {chosen_word}.')

for _ in range(word_length):
    display.append("_")
    
end_of_game = False
while not end_of_game:
    guess = input("Guess a Letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives-=1
        if lives == 0:
            print("You Lose.")
            end_of_game = True
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(hangman_art.stages[lives])