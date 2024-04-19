from flashy_interface import Flashy_UI
from data_manager import Data_Manager
from config import CARD_FRONT_IMG_PATH, CARD_BACK_IMG_PATH, BLACK, WHITE
import random
import sys
flashy_data = Data_Manager()
# ----- CONSTANTS ------------- #
DATA_SIZE = flashy_data.data_size()
# ----- GLOBALS --------------- #
incorrect = 0
seen = []
card_count = 0
# ----- NEXT CARD LOGIC ------- #
def next_card():
    global selected
    global timer
    flashy.after_cancel(timer)
    selected = random.choice(flashy_data.data_keys())
    while selected in seen:
        selected = random.choice(flashy_data.data_keys())
    seen.append(selected)
    flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_front)
    flashy.card_face.itemconfig(flashy.title, text = 'French', fill=BLACK)
    flashy.card_face.itemconfig(flashy.word, text=flashy_data.data['French'][selected], fill=BLACK)
    timer = flashy.after(3000, flip_card)

# ----- FLIP CARD LOGIC ------- #
def flip_card():
    flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_back)
    flashy.card_face.itemconfig(flashy.title, text='English', fill=WHITE)
    flashy.card_face.itemconfig(flashy.word, text=flashy_data.data['English'][selected], fill=WHITE)
# ----- CLICKED LOGIC --------- #
def clicked(event, correct):
    global incorrect
    global selected
    global card_count
    card_count += 1
    if not correct: incorrect += 1
    else: flashy_data.delete_data(selected)
    if card_count >= DATA_SIZE: 
        print("Finished")
        sys.exit(0)
    next_card()
# ----- USER INTERFACE -------- #
flashy = Flashy_UI()

# ----- UI BINDINGS ----------- #
flashy.right.bind('<Button-1>',func=lambda event: clicked(event, 1))
flashy.wrong.bind('<Button-1>',func=lambda event: clicked(event, 0))

timer = flashy.after(3000, flip_card)

selected = random.choice(flashy_data.data_keys())
while selected in seen:
    selected = random.choice(flashy_data.data_keys())
seen.append(selected)

flashy.card_face.itemconfig(flashy.card_image, image=flashy.card_front)
flashy.card_face.itemconfig(flashy.title, text = 'French', fill=BLACK)
flashy.card_face.itemconfig(flashy.word, text=flashy_data.data['French'][selected], fill=BLACK)

flashy.mainloop()