from tkinter import Tk, Button, Label, Entry, END
MKCONV = 1.609347

root = Tk()
root.minsize(width=200, height=100)
root.maxsize(width=400, height=100)
root.config(padx=15, pady=15)
root.title("Miles to Km Converter")

miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.grid(row=0,column=1)

miles_label = Label(text="Miles", anchor='w')
miles_label.grid(row=0,column=2)

is_equal_to_label = Label(text="is equal to", anchor='e')
is_equal_to_label.grid(row=1,column=0)

output_label = Label(text="0", anchor="center")
output_label.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

def out():
    miles = miles_entry.get()
    if miles:
        output_label.config(text=f'{int(miles)*MKCONV:.2f}')
    else:
        output_label.config(text="0")
    miles_entry.focus()
    miles_entry.select_range(0, END)


calulate_button = Button(text="Calculate", anchor='center', command=out)
calulate_button.grid(row=2, column=1)




root.mainloop()