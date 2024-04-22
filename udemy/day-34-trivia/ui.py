from tkinter import Button, Canvas, Label, Entry, PhotoImage, Tk
from config import THEME_COLOR, DISPLAY_COLOR, Q_FONT, S_FONT, TRUE_IMG, FALSE_IMG, RIGHT_COLOR, WRONG_COLOR
from quiz_brain import QuizBrain
import time

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text=f'Score: 0',
                                 justify='center',
                                 padx= 20,
                                 pady= 20,
                                 font= S_FONT,
                                 bg=THEME_COLOR,
                                 fg=DISPLAY_COLOR)
        self.score_label.grid(row=0,column=1,columnspan=1)

        self.canvas = Canvas(width=300,
                             height=250,
                             bg=DISPLAY_COLOR,
                             highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=Q_FONT,
                                                     width=280)
        self.canvas.grid(row=1,column=0,columnspan=2)

        true_image = PhotoImage(file=TRUE_IMG)
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2,column=0,columnspan=1,padx=20,pady=30)

        false_image = PhotoImage(file=FALSE_IMG)
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2,column=1,columnspan=1, padx=20, pady=30)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg=DISPLAY_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def true_pressed(self):
        is_right =  self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, correct):
        self.window.after(1000, func=self.get_next_question)
        if correct: self.canvas.config(bg=RIGHT_COLOR)
        else: self.canvas.config(bg=WRONG_COLOR)
