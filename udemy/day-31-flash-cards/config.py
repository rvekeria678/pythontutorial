import os
CURRENT_DIR = os.path.dirname(__file__)

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
DARK_GREEN = "#1D5B20"
CARD_FRONT_IMG_PATH = os.path.join(CURRENT_DIR, './images/card_front.png')
CARD_BACK_IMG_PATH = os.path.join(CURRENT_DIR, './images/card_back.png')
RIGHT_IMG_PATH = os.path.join(CURRENT_DIR, './images/right.png')
WRONG_IMG_PATH = os.path.join(CURRENT_DIR, './images/wrong.png')
TITLE_FONT = ("Ariel", 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
WAIT_TIME = 3000
DICTIONARY_PATH = os.path.join(CURRENT_DIR, './data/french_words.csv')
