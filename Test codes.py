from tkinter import *
import customtkinter


# Setup
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()

root.title("SDD Task 2")
root.geometry("600x600")
root.minsize(600, 600)


# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(8)), weight=10, uniform="a")



Quiz1_frame = Frame(root,padx = 10, pady =10,bg="blue")
Quiz1_frame.pack(fill ="both", expand = "True")


question_label = Label(Quiz1_frame, height=5, width=28, font= ("Arial", 20), bg="blue", wraplength=500)
question_label.pack 


option1 = Radiobutton(Quiz1_frame, bg="blue", font=("Arial", 20))
option2 = Radiobutton(Quiz1_frame, bg="blue", font=("Arial", 20))
option3 = Radiobutton(Quiz1_frame, bg="blue", font=("Arial", 20))
option4 = Radiobutton(Quiz1_frame, bg="blue", font=("Arial", 20))


option1.grid(row=1, column=0)
option2.grid(row=2, column=0)
option3.grid(row=3, column=0) 
option4.grid(row=4, column=0)



button_next = Button(Quiz1_frame, text="Next", bg="green", font=("Arial", 20)) 
button_next.grid(row=6, column=0) 








root.mainloop 

