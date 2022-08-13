#Import module for randomisation
import random

#To clear the screen after every answer

from replit import clear

#Importing the list of words for the game from another file
from words_hangman import word_list

#Importing the art for the game from another file
from art_hangman import stages, logo

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
word_lenght = (len(chosen_word))
lives = 6

#The goals is to great a variable with as much '_' as the letters in the chosen word
display = []
for _ in range(word_lenght):
    #or for letter in chosen_word:
    display += '_'

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word and if it is, replace the particular _ with the letter

end_of_game = False

print(logo)
while not end_of_game:
    guess = input("Chose a letter").lower()
  #to clear the screen after input
    clear()
  
    if guess in display:
      print (f"You've already guessed {guess}")
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print (f"{guess} isn't in the chosen word. You've lost a life")
        if lives == 0:
            end_of_game = True
            print("You lose")

    if '_' not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose!")

    print(stages[lives])
