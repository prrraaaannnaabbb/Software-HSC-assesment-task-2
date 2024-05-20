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