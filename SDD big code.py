from tkinter import*
import customtkinter
from tkinter import ttk

#Setup
root = customtkinter.CTk()


root.title("SDD Task 2")  
root.geometry("600x600")   
root.minsize(600,600)


#mainframe layout
frame = customtkinter.CTkFrame(master=root,fg_color="blue")
frame.grid(row = 500, column=50) 
Recognizing_shapes_frame = customtkinter.CTkFrame(master=root, width=100, height=300)



# #menu/page switching
def tab1():
    def tab2():
        label1.destroy()
        button_1.destroy() 
        label_2 = Label(root, text="second page", font =("Arial", 70))
        label_2.grid(row= 20, column=50)    
        def back():
            label_2.destroy()
            button_2.destroy() 
            tab1()
        button_2 = Button(root, text="Back", font=("Arial", 25), command=back) 
        button_2.grid(row= 20, column=50)  
    label1 = Label(root, text="Recognizing shapes", font=("Arial", 70))
    label1.grid(row= 20, column=50)  

    button_1 = Button(root, text="start", font=("Arial", 25), command=tab2) 
    button_1.grid(row= 20, column=50)  
tab1()    





root.mainloop() 