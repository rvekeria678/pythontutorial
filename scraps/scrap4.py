from tkinter import filedialog, Tk, Button

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file", file_path)
    else:
        print("No file selected.")


root = Tk()
root.title("File Selection")

select_button = Button(root, text="Select File", command=select_file)
select_button.pack(pady=20)

root.mainloop()



