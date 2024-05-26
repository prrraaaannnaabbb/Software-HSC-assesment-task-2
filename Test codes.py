from tkinter import*
from tkinter import messagebox

class QuizApp:
    def __init__(Quiz, root):
        Quiz.root = root
        Quiz.root.title("Quiz Application")
        Quiz.root.geometry("600x400")
        Quiz.root.configure(bg="#F7F7F7")

        Quiz.current_question = 0
        Quiz.score = 0

        Quiz.questions = [
{
    "question": "How many degrees in square",
    "options": ["A", "n", "g", "360"],
    "answer": "360"
},
{
    "question": "How many degrees in triangle",
    "options": ["yut", "n", "s", "180"],
    "answer": "180"
},
{
    "question": "What a trangle 3 sided",
    "options": ["8", "9", "g", "yes"],
    "answer": "yes"
},
{
    "question": "Is a square a quadrilateral",
    "options": ["7", "8", "yes", "11234"],
    "answer": "yes" 
},
{
    "question": "is a circle round",
    "options": ["7", "8", "yes", "11234"],
    "answer": "yes" 
}

]

        Quiz.create_widgets()

    def create_widgets(Quiz):
        Quiz.question_label = Label(Quiz.root, text="", font=("Arial", 16), bg="#F7F7F7", wraplength=500)
        Quiz.question_label.pack(pady=20)

        Quiz.option_vars = []
        Quiz.option_buttons = []

        for _ in range(4):
            var = StringVar()
            button = Radiobutton(Quiz.root, text="", variable=var, value="", font=("Arial", 14), bg="#F7F7F7", wraplength=500, indicatoron=False)
            Quiz.option_vars.append(var)
            Quiz.option_buttons.append(button)
            button.pack(fill=X, padx=20, pady=5)

        Quiz.submit_button = Button(Quiz.root, text="Submit", command=Quiz.check_answer, font=("Arial", 14), bg="#4CAF50", fg="white", relief=FLAT)
        Quiz.submit_button.pack(pady=20)

        Quiz.feedback_label = Label(Quiz.root, text="", font=("Arial", 14), bg="#F7F7F7")
        Quiz.feedback_label.pack(pady=10)

        Quiz.show_question()

    def show_question(Quiz):
        question = Quiz.questions[Quiz.current_question]
        Quiz.question_label.config(text=question["question"])

        for i, option in enumerate(question["options"]):
            Quiz.option_buttons[i].config(text=option, variable=Quiz.option_vars[Quiz.current_question], value=option)
            Quiz.option_vars[Quiz.current_question].set(None)

        Quiz.feedback_label.config(text="")

    def check_answer(Quiz):
        selected_option = Quiz.option_vars[Quiz.current_question].get()
        correct_answer = Quiz.questions[Quiz.current_question]["answer"]

        if selected_option == correct_answer:
            Quiz.score += 1
            Quiz.feedback_label.config(text="Correct!", fg="green")
        else:
            Quiz.feedback_label.config(text=f"Wrong! The correct answer was: {correct_answer}", fg="red")

        Quiz.current_question += 1

        if Quiz.current_question < len(Quiz.questions):
            Quiz.root.after(2000, Quiz.show_question)
        else:
            Quiz.root.after(2000, Quiz.show_result)

    def show_result(Quiz):
        messagebox.showinfo("Quiz Completed", f"Your score is: {Quiz.score}/{len(Quiz.questions)}")
        Quiz.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()  

