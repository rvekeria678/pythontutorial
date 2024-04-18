from flashy_interface import Flashy_UI
from dictionary import DATA
from config import CARD_FRONT_IMG_PATH, CARD_BACK_IMG_PATH, BLACK, WHITE
import random
import sys

# ----- CONSTANTS ------------- #
DATA_SIZE = len(DATA['French'])
# ----- GLOBALS --------------- #
incorrect = 0
pile = {i for i in range(DATA_SIZE)}
selected = -1
# ----- NEXT CARD LOGIC ------- #
def next_card():
    global selected
    selected = random.choice(list(pile))
    flashy.card_face.itemconfig(flashy.card_image, CARD_FRONT_IMG_PATH)
    flashy.card_face.itemconfig(flashy.title, text = 'French', fill = BLACK)
    flashy.word.face.itemconfig(flashy.word, DATA['French'][selected], fill = BLACK)

# ----- FLIP CARD LOGIC ------- #
def flip_card():
    flashy.card_face.itemconfig(flashy.card_image, CARD_FRONT_IMG_PATH)
    flashy.card_face.itemconfig(flashy.title, text = 'English', fill = WHITE)
    flashy.word.face.itemconfig(flashy.word, DATA['English'][selected], fill = WHITE)
# ----- CLICKED LOGIC --------- #
def clicked(event, correct):
    global incorrect
    
    if not correct: incorrect += 1
    else: pile.discard(selected)
    
    if not pile: sys.exit(0)
    
    next_card()

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

# ----- UI BINDINGS ----------- #
flashy.right.bind('<Button-1>',func=lambda event: clicked(event, 1))
flashy.wrong.bind('<Button-1>',func=lambda event: clicked(event, 0))

flashy.wrong.event_generate('<Button-1>')

flashy.mainloop()