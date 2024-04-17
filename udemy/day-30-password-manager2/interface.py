from tkinter import Tk, Label, Button, Entry, PhotoImage, Canvas, END, messagebox
import colors

LOCK_IMG_PATH = './logo.png'

class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=50,pady=50,bg=colors.WHITE)
        self.option_add('*Label.Background', colors.WHITE)
        
        #self.canvas = Canvas(width=200,height=200,bg=colors.WHITE, highlightthickness=0)
        #self.lock_img = PhotoImage(LOCK_IMG_PATH)
        #self.canvas.create_image(140,100, image=self.lock_img)
        #self.canvas.grid(row=0,column=1)



        self.mainloop()

    def on_enter(self, event):
        event.widget.config(bg=colors.RED, fg=colors.WHITE, cursor='hand2')

    def on_leave(self, event):
        event.widget.config(bg=colors.WHITE, fg=colors.BLACK, cursor='arrow')


my_passwordmanager = PasswordManager()