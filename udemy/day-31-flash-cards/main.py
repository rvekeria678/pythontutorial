from flashy_interface import Flashy_UI
from dictionary import DATA
from config import CARD_FRONT_IMG_PATH, CARD_BACK_IMG_PATH, BLACK, WHITE
import random
import sys
print(CARD_FRONT_IMG_PATH)
# ----- CONSTANTS ------------- #
DATA_SIZE = len(DATA['French'])
# ----- GLOBALS --------------- #
incorrect = 0
pile = {i for i in range(DATA_SIZE)}
selected = -1
# ----- NEXT CARD LOGIC ------- #
def next_card():
    global selected
    global timer
    flashy.after_cancel(timer)
    selected = random.choice(list(pile))
    flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_front)
    flashy.card_face.itemconfig(flashy.title, text = 'French', fill=BLACK)
    flashy.card_face.itemconfig(flashy.word, text=DATA['French'][selected], fill=BLACK)
    timer = flashy.after(3000, flip_card)

# ----- FLIP CARD LOGIC ------- #
def flip_card():
    flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_back)
    flashy.card_face.itemconfig(flashy.title, text='English', fill=WHITE)
    flashy.card_face.itemconfig(flashy.word, text=DATA['English'][selected], fill=WHITE)
# ----- CLICKED LOGIC --------- #
def clicked(event, correct):
    global incorrect
    if not correct: incorrect += 1
    else: pile.discard(selected)
    if not pile: sys.exit(0)
    next_card()
# ----- USER INTERFACE -------- #
flashy = Flashy_UI()

# ----- UI BINDINGS ----------- #
flashy.right.bind('<Button-1>',func=lambda event: clicked(event, 1))
flashy.wrong.bind('<Button-1>',func=lambda event: clicked(event, 0))

timer = flashy.after(3000, flip_card)

selected = random.choice(list(pile))
flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_front)
flashy.card_face.itemconfig(flashy.title, text = 'French', fill=BLACK)
flashy.card_face.itemconfig(flashy.word, text=DATA['French'][selected], fill=BLACK)

flashy.mainloop()