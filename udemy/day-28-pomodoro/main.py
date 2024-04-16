from tkinter import Label, Button, Image, Tk, Canvas, PhotoImage
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MARK = '✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    sessions_label.config(text='')

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minutes = 0, seconds = 0):
    if seconds < 0:
        seconds = 59
        minutes -= 1
    clock_display = f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    canvas.itemconfig(timer_text, text=clock_display)
    if minutes + seconds > 0:
        global timer
        timer = window.after(1000, count_down, minutes, seconds - 1)
    else:
        marks = '' 
        for rep in range(reps):
            if rep % 2 == 0:
                marks += MARK      
        sessions_label.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r'udemy\day-28-pomodoro\tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill='white', font=(FONT_NAME,30,'bold'))
canvas.grid(row=1,column=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME,40,'bold'))
title_label.grid(row=0,column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, padx=15, pady=6)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, padx=15, pady=6)
reset_button.grid(row=2, column=2)

sessions_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME,15,'bold'))
sessions_label.grid(row=3, column=1)

window.mainloop()