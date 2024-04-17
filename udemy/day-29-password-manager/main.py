from password_generator import generate_password
from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage
# --------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"
BLUE = "#9DA3FF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20, bg=WHITE)
root.option_add('*Label.Background', WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file=r'udemy\day-29-password-manager\logo.png')
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

generate_button = Button(text="Generate Password", width=14)
add_button = Button(text="Add", width=36)

website_input = Entry(width=35, justify="left", highlightbackground=BLUE)
username_input = Entry(width=35, justify="left", highlightbackground=BLUE)
password_input = Entry(width=21, justify="left", highlightbackground=BLUE)

website_label.grid(row=1,column=0)
email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)

website_input.grid(row=1,column=1,columnspan=2)
username_input.grid(row=2,column=1, columnspan=2)
password_input.grid(row=3, column=1)

generate_button.grid(row=3,column=2)
add_button.grid(row=4,column=1, columnspan=2)




root.mainloop()