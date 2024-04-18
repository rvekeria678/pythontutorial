from tkinter import Tk, Button, Canvas, PhotoImage, Label, ALL, TclError
from config import BACKGROUND_COLOR, WHITE, CARD_FRONT_IMG_PATH, CARD_BACK_IMG_PATH, TITLE_FONT, WORD_FONT, DARK_GREEN, RIGHT_IMG_PATH, WRONG_IMG_PATH

# ---- GLOBALS ---- #
card_toggle = False

class Flashy_UI(Tk):
    def __init__(self):
        super().__init__()
        self.title('Flashy')
        self.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
        self.option_add('*Label.Background', BACKGROUND_COLOR)

        self.create_widgets()
        self.arrange_widgets()

    def create_widgets(self):
        self.card_face = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
        self.right = Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.wrong = Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
        try:
            self.card_front = PhotoImage(file=CARD_FRONT_IMG_PATH)
            self.card_back = PhotoImage(file=CARD_BACK_IMG_PATH)
            self.right_img = PhotoImage(file=RIGHT_IMG_PATH)
            self.wrong_img = PhotoImage(file=WRONG_IMG_PATH)
        except TclError:
            print("Failed to load resources for card faces.")
            self.card_front = self.card_face.create_rectangle(0,0,250,150, fill=WHITE)
        else:
            self.card_image = self.card_face.create_image(400, 263, image = self.card_front)
            self.right.create_image(50,50,image = self.right_img)
            self.wrong.create_image(50,50,image = self.wrong_img)
        finally:
            self.title = self.card_face.create_text(400,150,
                                                 text='Title',
                                                 font=TITLE_FONT,
                                                 anchor='center')
            self.word = self.card_face.create_text(400,263,
                                                text='Word', 
                                                font=WORD_FONT,
                                                anchor='center')

    def arrange_widgets(self):
        self.card_face.grid(row=0,column=0, columnspan=2)
        self.right.grid(row=1,column=0, pady=20)
        self.wrong.grid(row=1, column=1, pady=20)

    def flip(self):
        global card_toggle
        if card_toggle:
            self.card_face.itemconfig(self.card_image, image=self.card_back)
            card_toggle = False
        else:
            self.card_face.itemconfig(self.card_image, image=self.card_front)
            card_toggle = True