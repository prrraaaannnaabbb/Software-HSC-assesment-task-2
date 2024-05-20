# import tkinter as tk
# from tkinter import messagebox, ttk
# from ttkbootstrap import Style


# quiz_data = [
#     {
#         "question": "What is the capital of France?",
#         "choices": ["Paris", "London", "Berlin", "Madrid"],
#         "answer": "Paris"
#     },
#     {
#         "question": "What is the largest planet in our solar system?",
#         "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
#         "answer": "Jupiter"
#     },
#     {
#         "question": "What is the chemical symbol for gold?",
#         "choices": ["Go", "Au", "Ag", "Gd"],
#         "answer": "Au"
#     },
#     {
#         "question": "Which country is known as the 'Land of the Rising Sun'?",
#         "choices": ["China", "Japan", "South Korea", "Thailand"],
#         "answer": "Japan"
#     }
#     # Add more questions here
# ]




# # Function to display the current question and choices
# def show_question():
#     # Get the current question from the quiz_data list
#     question = quiz_data[current_question]
#     qs_label.config(text=question["question"])

#     # Display the choices on the buttons
#     choices = question["choices"]
#     for i in range(4):
#         choice_btns[i].config(text=choices[i], state="normal") # Reset button state

#     # Clear the feedback label and disable the next button
#     feedback_label.config(text="")
#     next_btn.config(state="disabled")

# # Function to check the selected answer and provide feedback
# def check_answer(choice):
#     # Get the current question from the quiz_data list
#     question = quiz_data[current_question]
#     selected_choice = choice_btns[choice].cget("text")

#     # Check if the selected choice matches the correct answer
#     if selected_choice == question["answer"]:
#         # Update the score and display it
#         global score
#         score += 1
#         score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
#         feedback_label.config(text="Correct!", foreground="green")
#     else:
#         feedback_label.config(text="Incorrect!", foreground="red")
    
#     # Disable all choice buttons and enable the next button
#     for button in choice_btns:
#         button.config(state="disabled")
#     next_btn.config(state="normal")

# # Function to move to the next question
# def next_question():
#     global current_question
#     current_question +=1

#     if current_question < len(quiz_data):
#         # If there are more questions, show the next question
#         show_question()
#     else:
#         # If all questions have been answered, display the final score and end the quiz
#         messagebox.showinfo("Quiz Completed",
#                             "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
#         root.destroy()

# # Create the main window
# root = tk.Tk()
# root.title("Quiz App")
# root.geometry("600x500")
# style = Style(theme="flatly")

# # Configure the font size for the question and choice buttons
# style.configure("TLabel", font=("Helvetica", 20))
# style.configure("TButton", font=("Helvetica", 16))

# # Create the question label
# qs_label = ttk.Label(
#     root,
#     anchor="center",
#     wraplength=500,
#     padding=10
# )
# qs_label.pack(pady=10)

# # Create the choice buttons
# choice_btns = []
# for i in range(4):
#     button = ttk.Button(
#         root,
#         command=lambda i=i: check_answer(i)
#     )
#     button.pack(pady=5)
#     choice_btns.append(button)

# # Create the feedback label
# feedback_label = ttk.Label(
#     root,
#     anchor="center",
#     padding=10
# )
# feedback_label.pack(pady=10)

# # Initialize the score
# score = 0

# # Create the score label
# score_label = ttk.Label(
#     root,
#     text="Score: 0/{}".format(len(quiz_data)),
#     anchor="center",
#     padding=10
# )
# score_label.pack(pady=10)

# # Create the next button
# next_btn = ttk.Button(
#     root,
#     text="Next",
#     command=next_question,
#     state="disabled"
# )
# next_btn.pack(pady=10)

# # Initialize the current question index
# current_question = 0

# # Show the first question
# show_question()

# # Start the main event loop
# root.mainloop() 






from tkinter import *
import customtkinter


# Setup
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()

root.title("SDD Task 2")
root.geometry("600x600")
root.minsize(600, 600)


# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(8)), weight=10, uniform="a")












#Main menu widgets
def tab_main_menu_widgets():
    global label1, button_Quiz, button_Lessons
    label1 = Label(root, text="Recognizing shapes", font=("Arial", 60))
    label1.grid(column=3, row=0, columnspan = 12)    

    button_Lessons = Button(root, text="Lessons", font=("Arial", 25),command = tab_Lesson_menu ) 
    button_Lessons.grid(column=6, row =1, columnspan= 4)  
           
    button_Quiz = Button(root, text="Quiz!", font=("Arial", 25), command=tab_Quiz_menu) 
    button_Quiz.grid(column=8, row=1, columnspan = 4)   





#Lessons_page
def tab_Lesson_menu():
    global label_2, button_triangles, button_quads, button_non_polygon, button_polygons
    label1.destroy()
    button_Lessons.destroy()  
    button_Quiz.destroy()
    label_2 = Label(root, text="Lessons", font =("Arial", 60))
    label_2.grid(column=2, row=0, columnspan = 12)   
    def back():
            label_2.destroy()
            backb1.destroy()
            button_triangles.destroy() 
            button_quads.destroy()  
            button_polygons.destroy() 
            button_non_polygon.destroy() 
            tab_main_menu_widgets()  
    backb1 = Button(root, text="Back", font=("Arial", 25), command=back) 
    backb1.grid(column=0, row =0, columnspan = 4)  

    #Lessons buttons opening their respective lesson
    button_triangles = Button(root, text="Triangles", font=("Arial", 25)) 
    button_triangles.grid(column=4, row =1, columnspan= 4) 

    button_quads = Button(root, text="Quadrilaterals", font=("Arial", 25)) 
    button_quads.grid(column=8, row =1, columnspan= 4) 

    button_polygons = Button(root, text="Polygons", font=("Arial", 25)) 
    button_polygons.grid(column=4, row =2, columnspan= 4) 

    button_non_polygon = Button(root, text="Non-Polygons", font=("Arial", 25)) 
    button_non_polygon.grid(column=8, row =2, columnspan= 4) 












#Quiz_page
def tab_Quiz_menu(): 
    global label_3rdpage, button_q1,backb2
    label1.destroy()
    button_Lessons.destroy() 
    button_Quiz.destroy() 
    label_3rdpage = Label(root, text="Quiz!!", font =("Arial", 60))
    label_3rdpage.grid(column=3, row=0, columnspan = 12)     

    #Quiz buttons inside Quiz_page starting the exam
    button_q1 = Button(root, text ="Quiz 1", font=("Arial", 25), command=tabquiz1) 
    button_q1.grid(column=4, row =1, columnspan= 4)  
    def back2(): 
                label_3rdpage.destroy()
                backb2.destroy()
                button_q1.destroy() 
                tab_main_menu_widgets() 

    backb2 = Button(root, text="Back", font=("Arial", 25), command=back2) 
    backb2.grid(column=0, row =0, columnspan = 4)  




    

    


#Quiz 1 exam 
def tabquiz1(): 
    global label_q1page
    label_3rdpage.destroy() 
    backb2.destroy() 
    button_q1.destroy()
    label_q1page = Label(root, text="Quiz 1!", font =("Arial", 60))
    label_q1page.grid(column=3, row=0, columnspan = 12) 
    def back3(): 
                    label_q1page.destroy() 
                    backb3.destroy()
                    tab_Quiz_menu()

    backb3 = Button(root, text="Back", font=("Arial", 25), command = back3) 
    backb3.grid(column=0, row =0, columnspan = 4)  

    
        


    


#main menu
def tab_main_menu(): 
    tab_main_menu_widgets()
tab_main_menu()


















    




root.mainloop() 