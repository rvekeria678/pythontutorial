from password_generator import generate_password
from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file=r'udemy\day-29-password-manager\logo.png')
canvas.create_image(100,100, image=lock_img)
canvas.pack()

root.mainloop()