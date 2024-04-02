# Hangman

import random

word_bank = ['aardvark', "baboon", "camel"]


def driver():
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         
          ''')
    #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
    chosen_word = random.choice(word_bank)

    #TODO-2 - Ask the user to guess a letter an assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chose_word
    for character in chosen_word:
        if guess == character:
            print("Right")
        else:
            print("Wrong")


driver()