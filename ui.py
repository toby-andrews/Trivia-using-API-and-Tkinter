from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    global points
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width= 250, text="test", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)


        self.score = Label(text=f"Score: {0}")
        self.score.config(bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=self.user_answered_true)
        self.true.grid(column=0, row=2)

        #Don't need to use self with image as it is not being accessed anywhere else

        false_image = PhotoImage(file="./images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=self.user_answered_false)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions() == False:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz. Your final score was {self.quiz.score}!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
        else:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)


    def user_answered_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_answered_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
