# Hangman

import random
import hangmanui

word_bank = ['aardvark', "baboon", "camel"]


def driver():
    # Presets
    stage = 0
    chosen_word = random.choice(word_bank)
    game_complete = False
    display = ['_'] * len(chosen_word)
    lives = 5

    # Title Screen
    print(hangmanui.title)

    while not game_complete:
        print(hangmanui.stages[stage])
        print(' '.join(display))
        guess = input("Guess a Letter: ")
    
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
            
        if guess not in chosen_word:
            lives -= 1
            stage += 1
        
        if '_' not in display:
            print(hangmanui.won_screen)
            game_complete = True

        if lives <= 0:
            print(hangmanui.lose_screen)
            game_complete = True



driver()