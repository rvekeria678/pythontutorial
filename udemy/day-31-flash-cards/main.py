from flashy_interface import Flashy_UI
from dictionary import DATA
import random

# ----- CONSTANTS ------------- #
DATA_SIZE = len(DATA['French'])
# ----- GLOBALS --------------- #
incorrect = 0
pile = {i for i in range(DATA_SIZE)}
current_word = -1
# ----- RESET LOGIC ----------- #
def reset():
    pile = {i for i in range(DATA_SIZE)}
# ----- SELECT WORD LOGIC ----- #
def select_word():
    return random.choice(pile)
# ----- REMOVAL LOCIC --------- #
def remove_card(event):
    flashy.flip()
# ----- ADJUST SCORING -------- #
def update_score(event):
    incorrect += 1
# ----- UI -------------------- #
flashy = Flashy_UI()

# ----- UI BINDINGS ----------- #
flashy.right.bind('<Button-1>',func=remove_card)
flashy.wrong.bind('<Button-1>',func=update_score)

flashy.mainloop()