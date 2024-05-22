









import tkinter as tk 


root =tk.Tk() 
root.geometry("500x500") 



questions = ["1 + 1 = ?","2 + 2 = ?", "3 + 3 = ?", "4 + 4 = ?","5 + 5 = ?", ] 

options = [["A","B","2","C","2"],
           ["A","4","V","C","4"],
           ["A","B","Z","6","6"],
           ["8","B","D","C","8"],
           ["D","10","A","C","10"],
         ]




frame = tk.Frame(padx = 10, pady =10,bg="blue")
frame.pack(fill ="both", expand = "True")


question_label = tk.Label(frame, height=5, width=28, font= ("Verdana", 20), bg="blue", wraplength=500)
question_label.grid(row =0, column = 0)


option1 = tk.Radiobutton(frame, bg="blue", font=("Verdana'", 20))
option2 = tk.Radiobutton(frame, bg="blue", font=("Verdana", 20))
option3 = tk.Radiobutton(frame, bg="blue", font=("Verdana", 20))
option4 = tk.Radiobutton(frame, bg="blue", font=("Verdana", 20))


option1.grid(row=1, column=0)
option2.grid(row=2, column=0)
option3.grid(row=3, column=0) 
option4.grid(row=4, column=0)



button_next = tk.Button(frame, text="Next", bg="green", font=("Verdana, 20")) 
button_next.grid(row=6, column=0) 








root.mainloop