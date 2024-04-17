from password_generator import generate_password
from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage
# --------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"
BLUE = "#9DA3FF"
RED = "#E14949"
BLACK = "#000000"
FONT = ('Arial', 10, 'bold')
INPUT_FONT = ('Arial', 13)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# ---- Button Events ---- #
def on_enter(event):
    event.widget.config(bg=RED, fg='white', cursor="hand2")

def on_leave(event):
    event.widget.config(bg=WHITE, fg=BLACK, cursor='arrow')

root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=25, bg=WHITE)
root.option_add('*Label.Background', WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file=r'udemy\day-29-password-manager\logo.png')
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

generate_button = Button(text="Generate Password", 
                         width=14, 
                         bg=WHITE,
                         font=FONT,
                         padx=10)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)
add_button = Button(text="Add", 
                    width=36, 
                    bg=WHITE,
                    font=FONT)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

website_input = Entry(width=35, font=INPUT_FONT)
username_input = Entry(width=35, font=INPUT_FONT)
password_input = Entry(width=21, font=INPUT_FONT)

# ------------------------ Grid Formatting ------------------------ #

website_label.grid(row=1,column=0)
email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)

website_input.grid(row=1,column=1,columnspan=2, sticky='ew')
username_input.grid(row=2,column=1, columnspan=2, sticky='ew')
password_input.grid(row=3, column=1, columnspan=1, sticky='ew')

generate_button.grid(row=3,column=2, padx=5)
add_button.grid(row=4,column=1, columnspan=2, pady=10, sticky='ew')




root.mainloop()