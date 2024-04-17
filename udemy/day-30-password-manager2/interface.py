from tkinter import Tk, Label, Button, Entry, PhotoImage, Canvas, END, messagebox, TclError
import colors

# ----- CONSTANTS ----- #
FONT = ('Arial', 10, 'normal')
INPUT_FONT = ('Arial', 13)
LOCK_IMG_PATH = r'C:\Users\rveke\OneDrive\Documents\GitHub\pythontutorial\udemy\day-30-password-manager2\logo.png'

class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=50,pady=50,bg=colors.WHITE)
        self.option_add('*Label.Background', colors.WHITE)

        self.create_widgets()
        self.arrange_widgets()

    def create_widgets(self):
        self.canvas = Canvas(width=200,height=200,bg=colors.WHITE, highlightthickness=0)
        try:
            self.lock_img = PhotoImage(file=LOCK_IMG_PATH)
            self.canvas.create_image(140,100, image=self.lock_img)
        except TclError:
            self.canvas.create_rectangle(0,0,250,150,fill=colors.RED)
        finally:
            self.website_label = Label(text="Website:")
            self.email_username_label = Label(text="Email/Username:")
            self.password_label = Label(text="Password:")

            self.search_button = Button(text="Search", 
                                      width=14, 
                                      bg=colors.WHITE,
                                      font=FONT,
                                      padx=10,
                                      activebackground=colors.LIGHT_RED,
                                      activeforeground=colors.WHITE,
                                      relief="groove")
            self.search_button.bind("<Enter>", self.on_enter)
            self.search_button.bind("<Leave>", self.on_leave)                       
            self.generate_button = Button(text="Generate Password", 
                                      width=14, 
                                      bg=colors.WHITE,
                                      font=FONT,
                                      padx=10,
                                      activebackground=colors.LIGHT_RED,
                                      activeforeground=colors.WHITE,
                                      relief="groove")
            self.generate_button.bind("<Enter>", self.on_enter)
            self.generate_button.bind("<Leave>", self.on_leave)
            self.add_button = Button(text="Add", 
                                 width=36, 
                                 bg=colors.WHITE,
                                 font=FONT,
                                 activebackground=colors.LIGHT_RED,
                                 activeforeground=colors.WHITE,
                                 relief='groove')
            self.add_button.bind("<Enter>", self.on_enter)
            self.add_button.bind("<Leave>", self.on_leave)

            self.website_input = Entry(width=35,
                                   font=INPUT_FONT,
                                   relief='solid',)
            self.website_input.focus()
            self.username_input = Entry(width=35,
                                    font=INPUT_FONT,
                                    relief='solid')
            self.username_input.insert(END,'rvekeria678@gmail.com')
            self.password_input = Entry(width=21,
                                    font=INPUT_FONT,
                                    relief='solid')
    def arrange_widgets(self):
        self.canvas.grid(row=0,column=1)

        self.website_label.grid(row=1,column=0)
        self.email_username_label.grid(row=2,column=0)
        self.password_label.grid(row=3,column=0)

        self.website_input.grid(row=1,column=1,columnspan=1, pady=5, sticky='ew')
        self.username_input.grid(row=2,column=1, columnspan=2, pady=5, sticky='ew')
        self.password_input.grid(row=3, column=1, columnspan=1, pady=5, sticky='ew')

        self.search_button.grid(row=1,column=2, padx=5)
        self.generate_button.grid(row=3,column=2, padx=5)
        self.add_button.grid(row=4,column=1, columnspan=2, pady=7, sticky='ew')
    
    def on_enter(self, event):
        event.widget.config(bg=colors.RED, fg=colors.WHITE, cursor='hand2')

    def on_leave(self, event):
        event.widget.config(bg=colors.WHITE, fg=colors.BLACK, cursor='arrow')
    
    def confirm_entry_message(self):
        return messagebox.askokcancel(title=self.website_input.get(),message=f'These are the details entered: \nEmail: {self.username_input.get()}\nPassword: {self.password_input.get()}\nIs it ok to save?')
    
    def missing_info_message(self):
        messagebox.showerror(title="Password Manager", message="Opps! There is some missing information!")

    def missing_resources_message(self):
        messagebox.showerror(title="Password Manager", message="Oops. Missing Resources ):")

    def file_missing(self):
        messagebox.showinfo(title="Password manager", message='File Does Not Exist')

    def website_credentials(self, username, password):
        messagebox.showinfo(title="Password Manager", message=f"{self.website_input.get()} Credentials:\nEmail: {username}\nPassword: {password}")

    def website_not_found_message(self):
        messagebox.showinfo(title="Password Manager", message=f"You do not have credentials for {self.website_input.get()}.")

    def clear_website_input(self):
        self.website_input.delete(0,END)
    
    def clear_password_input(self):
        self.password_input.delete(0,END)

    def fill_password_input(self, password):
        self.password_input.insert(END, password)