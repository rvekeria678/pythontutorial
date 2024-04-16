import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=('Arial', 24, 'bold'))

my_label.pack()


window.mainloop()

foo = lambda *args: [x*x for x in args if x % 2 == 0]

print(foo(1,2,3,4,5,6,7,8,9,10))