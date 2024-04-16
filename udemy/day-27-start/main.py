from tkinter import Tk, Label, Button, Entry, Listbox

FONT = ('Arial', 24, 'bold')

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

label1 = Label(text="Title Text", font=FONT)
label1.grid(column=0,row=0)

button1 = Button(text="Enter")
button1.grid(column=2,row=0)

button2 = Button(text="Add Something")
button2.grid(column=1,row=1)

entry1 = Entry()
entry1.grid(column=3,row=2)
"""
# Label
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.place(x=100,y=200)

my_label['text'] = 'New Text'
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command= button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()
print(input.get())
"""

window.mainloop()

