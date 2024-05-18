from tkinter import*
import customtkinter
from tkinter import ttk

#Setup
root = customtkinter.CTk()

root.title("SDD Task 2")  
root.geometry("600x600")   
root.minsize(600,600)

#define grid 
root.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight = 10, uniform = "a")
root.rowconfigure((0,1,2,3,4,5,6,7), weight = 10, uniform="a")




#main menu
def tab1(): 
    #Lessons_page
    def tab2():
        label1.destroy()
        button_Lessons.destroy()  
        button_Quiz.destroy()
        label_2 = Label(root, text="Lessons", font =("Arial", 60))
        label_2.grid(column=2, row=0, columnspan = 12)      
        def back():
            label_2.destroy()
            backb1.destroy() 
            tab1()
        backb1 = Button(root, text="Back", font=("Arial", 25), command=back) 
        backb1.grid(column=0, row =0, columnspan = 4)  





        #Lessons buttons opening thier respective lesson
        button_triangles = Button(root, text="Triangles", font=("Arial", 25)) 
        button_triangles.grid(column=4, row =1, columnspan= 4) 

        button_quads = Button(root, text="Qudrilaterals", font=("Arial", 25)) 
        button_quads.grid(column=8, row =1, columnspan= 4) 

        button_polygons = Button(root, text="Polygons", font=("Arial", 25)) 
        button_polygons.grid(column=4, row =2, columnspan= 4) 

        button_non_polygon = Button(root, text="Non-Polygons", font=("Arial", 25)) 
        button_non_polygon.grid(column=8, row =2, columnspan= 4) 
    




    label1 = Label(root, text="Recognizing shapes", font=("Arial", 60))
    label1.grid(column=3, row=0, columnspan = 12)    

    button_Lessons = Button(root, text="Lessons", font=("Arial", 25), command=tab2) 
    button_Lessons.grid(column=6, row =1, columnspan= 4)  




    #Quiz_page
    def tab3(): 
        label1.destroy()
        button_Lessons.destroy() 
        button_Quiz.destroy() 
        label_3rdpage = Label(root, text="Quiz!!", font =("Arial", 60))
        label_3rdpage.grid(column=3, row=0, columnspan = 12)     
        def back(): 
            label_3rdpage.destroy()
            backb2.destroy() 
            tab1() 
        backb2 = Button(root, text="Back", font=("Arial", 25), command=back) 
        backb2.grid(column=0, row =0, columnspan = 4)   
          
    button_Quiz = Button(root, text="Quiz!", font=("Arial", 25), command=tab3) 
    button_Quiz.grid(column=8, row=1, columnspan = 4)    
tab1()      




root.mainloop() 