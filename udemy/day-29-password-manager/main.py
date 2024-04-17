from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, END, messagebox
import pyperclip
# --------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"
BLUE = "#9DA3FF"
RED = "#E14949"
LIGHT_RED = "#DF6C6C"
BLACK = "#000000"
GRAY = "#818181"
FONT = ('Arial', 10, 'normal')
INPUT_FONT = ('Arial', 13)
GENERATED_PASSWORD_LENGTH = 15
DATA_FILE_PATH = r'C:\Users\rveke\OneDrive\Documents\GitHub\pythontutorial\udemy\day-29-password-manager\data.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import generate_password
def fill_password():
    password_input.delete(0,END)
    new_password = generate_password(GENERATED_PASSWORD_LENGTH)
    password_input.insert(END,new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website, user, password = website_input.get(), username_input.get(), password_input.get()

    if website and user and password:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {user}\nPassword: {password}\nIs it ok to save?')
        
        if is_ok:
            with open(DATA_FILE_PATH, 'a') as data_file:
                data_file.write(f'{website} | {user} | {password}\n')
            # Clear Inputs
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showerror(title="Password Manager", message="Oops! There is some missing information!")
# ---------------------------- UI SETUP ------------------------------- #
# ---- Button Events ---- #
def on_enter(event):
    event.widget.config(bg=RED, fg='white', cursor="hand2")

def on_leave(event):
    event.widget.config(bg=WHITE, fg=BLACK, cursor='arrow')
# ---- Window Setup ---- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50, bg=WHITE)
root.option_add('*Label.Background', WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file=r'udemy\day-29-password-manager\logo.png')
canvas.create_image(140,100, image=lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

generate_button = Button(command=fill_password,
                         text="Generate Password", 
                         width=14, 
                         bg=WHITE,
                         font=FONT,
                         padx=10,
                         activebackground=LIGHT_RED,
                         activeforeground=WHITE,
                         relief="groove")
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)
add_button = Button(command=save_password,
                    text="Add", 
                    width=36, 
                    bg=WHITE,
                    font=FONT,
                    activebackground=LIGHT_RED,
                    activeforeground=WHITE,
                    relief='groove')
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

website_input = Entry(width=35,
                      font=INPUT_FONT,
                      relief='solid',)
website_input.focus()
username_input = Entry(width=35,
                       font=INPUT_FONT,
                       relief='solid')
username_input.insert(END,'rvekeria678@gmail.com')
password_input = Entry(width=21,
                       font=INPUT_FONT,
                       relief='solid')

# ------------------------ Grid Formatting ------------------------ #

website_label.grid(row=1,column=0)
email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)

website_input.grid(row=1,column=1,columnspan=2, pady=5, sticky='ew')
username_input.grid(row=2,column=1, columnspan=2, pady=5, sticky='ew')
password_input.grid(row=3, column=1, columnspan=1, pady=5, sticky='ew')

generate_button.grid(row=3,column=2, padx=5)
add_button.grid(row=4,column=1, columnspan=2, pady=7, sticky='ew')

root.mainloop()