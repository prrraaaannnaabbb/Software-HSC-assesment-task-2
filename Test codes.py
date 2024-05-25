from tkinter import *
import customtkinter
from Quiz_data import quiz_data

# Setup
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()

root.title("SDD Task 2")
root.geometry("600x600")
root.minsize(600, 600)


#Quiz1
Quiz1_frame = Frame(root,padx = 10, pady =10,)
Quiz1_frame.pack(fill = "both", expand = True)


# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(18)), weight=10, uniform="a") 


#Initalise score and question number
score = 0 
currentq =0 

def Next_question(): 
    pass



def answer_check(Anscheck): 
    pass 

def increment_score(): 
    pass

def diable_buttons(state): 
    pass
    # optionA["state"] = state 
    # optionB["state"] = state        
    # optionC["state"] = state 
    # optionD["state"] = state 



question_label = Label(Quiz1_frame, height=20, width=45, font= ("Arial", 20), bg="grey", wraplength=500)
question_label.grid(row= 0, column =2)








optionA = customtkinter.CTkRadioButton(
    Quiz1_frame,
    radiobutton_width=15,
    radiobutton_height= 15,
    text = quiz_data[currentq],
    command = answer_check
                            ) 

optionB = customtkinter.CTkRadioButton(
    Quiz1_frame,
    radiobutton_width=15,
    radiobutton_height= 15,
    text = quiz_data[currentq],
    command = answer_check
                            )
 
optionC = customtkinter.CTkRadioButton(
    Quiz1_frame,
    radiobutton_width=15,
    radiobutton_height= 15,
    text = quiz_data[currentq],
    command = answer_check
                            ) 

optionD= customtkinter.CTkRadioButton(
    Quiz1_frame,
    radiobutton_width=15,
    radiobutton_height= 15,
    text = quiz_data[currentq],
    command = answer_check
                            ) 

optionA.grid(sticky="W", row=6, column=1)
optionB.grid(sticky="W",row=8, column=1)
optionC.grid(sticky="W",row=10, column=1) 
optionD.grid(sticky="W",row=12, column=1) 




button_next = Button(Quiz1_frame, text="Next", bg="pink", font=("Arial", 40), command =Next_question) 
button_next.grid(row=18, column=2) 










root.mainloop 

