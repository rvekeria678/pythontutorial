from flashy_interface import Flashy_UI
from dictionary import DATA
import random
import sys

# ----- CONSTANTS ------------- #
DATA_SIZE = len(DATA['French'])
# ----- GLOBALS --------------- #
incorrect = 0
pile = {i for i in range(DATA_SIZE)}
selected = random.choice(list(pile))
# ----- SELECT WORD LOGIC ----- #
def select_word():
    return random.choice(pile)
# ----- CLICKED LOGIC --------- #
def clicked(event, correct):
    global incorrect
    global selected
    if not correct: incorrect += 1
    else: pile.discard(selected)
    if pile: selected = random.choice(list(pile))
    else: sys.exit(0)
    flashy.flip(DATA['French'][selected])
    flashy.after(3000, flashy.flip, DATA['English'][selected])
    print(len(pile))

# ----- ENABLE BUTTONS -------- #
def enable_buttons():
    flashy.right.bind('<Button-1>',func=lambda event: clicked(event, 1))
    flashy.wrong.bind('<Button-1>',func=lambda event: clicked(event, 0))
# ----- DISABLE BUTTONS ------- #
def disable_buttons():
    flashy.right.unbind('<Button-1>')
    flashy.wrong.unbind('<Button-1>')
# ----- USER INTERFACE -------- #
flashy = Flashy_UI()

flashy.card_face.itemconfig(flashy.word, text=DATA['English'][selected])

# ----- UI BINDINGS ----------- #
flashy.right.bind('<Button-1>',func=lambda event: clicked(event, 1))
flashy.wrong.bind('<Button-1>',func=lambda event: clicked(event, 0))

flashy.mainloop()