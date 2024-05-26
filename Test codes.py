



#before a.i debugging
from tkinter import *
from tkinter import messagebox
import customtkinter
from ttkbootstrap.scrolled import ScrolledFrame
from Triangles_data1 import Triangles1
from Triangles_data2 import Triangles2
from Square_data1 import Square1 
from Square_data2 import Square2 




# Setup
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk() 

# app_width = 600 
# app_height = 600

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)



# root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

root.title("SDD Task 2")
root.geometry("600x600")
root.minsize(600, 600)




# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(12)), weight=10, uniform="a")




#inclusivity features 

# Theme Change Functions
def update_widget_colors(bg, fg, entry_bg, button_bg, button_fg):
    for widget in root.winfo_children():
        if isinstance(widget, Label):
            widget.config(bg=bg, fg=fg)
        elif isinstance(widget, Entry):
            widget.config(bg=entry_bg, fg=fg)
        elif isinstance(widget, Button):
            widget.config(bg=button_bg, fg=button_fg)
        elif isinstance(widget, ScrolledFrame):
            for subwidget in widget.winfo_children():
                subwidget.config(bg=bg, fg=fg)
    root.update() 






#Menu Bar Options (Inclusivity Features)
my_menu = Menu(root)
root.config(menu=my_menu) 

    #File Menu Item (Quits the program)
file_menu = Menu(my_menu) 
my_menu.add_cascade(label = "options", menu=file_menu) 
file_menu.add_command(label="Exit", command=root.quit) 



def beige_theme():
    root.config(bg="#F5E0C0")
    update_widget_colors("#F5E0C0", "black", "#D9CCA2", "#BEEEA0", "black")   

def navy_theme():
    root.config(bg="#2C3E50")
    update_widget_colors("#2C3E50", "white", "#34495E", "#E74C3C", "white")

def burgundy_theme():
    root.config(bg="#800020")
    update_widget_colors("#672F25", "white", "grey", "#c4a747", "black")

def light_aqua_theme():
    root.config(bg="#A2C4C9")
    update_widget_colors("#A2C4C9", "black", "grey", "#8FCACF", "black")

def botanical_theme():
    root.config(bg="#446725")
    update_widget_colors("#D0E2C8", "black", "#F2F7EF", "#D198C0", "#4F2743")

def dark_theme():
    root.config(bg="#7F7C7E")
    update_widget_colors("#333333", "white", "white", "#ADD8E6", "#7F7C7E")

def honey_theme():
    root.config(bg="#EECC64")
    update_widget_colors("#FDEB71", "black", "#FFFCDB", "#FFB03B", "black")

def chestnut_theme():
    root.config(bg="#5E4420")
    update_widget_colors("#5E4420", "white", "#8D6D49", "#C98E3F", "white")

def light_theme():
    root.config(bg="white")
    update_widget_colors("white", "black", "white", "black", "white")


















Themes_menu = Menu(my_menu) 
my_menu.add_cascade(label="Themes", menu = Themes_menu) 
Themes_menu.add_command(label="Dark", command =dark_theme) 
Themes_menu.add_command(label="Light", command = light_theme) 
Themes_menu.add_command(label="Chestnut", command = chestnut_theme ) 
Themes_menu.add_command(label="Navy", command = navy_theme)  
Themes_menu.add_command(label="Beige", command = beige_theme)
Themes_menu.add_command(label="Burgundy", command = burgundy_theme) 
Themes_menu.add_command(label="Light Aqua", command = light_aqua_theme) 
Themes_menu.add_command(label="Botanical", command = botanical_theme) 
Themes_menu.add_command(label="Honey", command = honey_theme)




# Font Change Function
def set_font(new_font, new_font_size):
    font_tuple = (new_font, new_font_size)
    for widget in root.winfo_children():
        widget.config(font=font_tuple)
    root.update()



def zoom_in():
    global current_font_size
    current_font_size += 2
    set_font(current_font, current_font_size)

def zoom_out():
    global current_font_size
    current_font_size = max(current_font_size - 2, 1)
    set_font(current_font, current_font_size)



# Fonts Menu (Changes the Font of the GUI)
Fonts_menu = Menu(my_menu)
my_menu.add_cascade(label="Fonts", menu=Fonts_menu)
Fonts_menu.add_command(label="Helvetica", command=lambda: set_font("Helvetica", current_font_size))
Fonts_menu.add_command(label="Arial", command=lambda: set_font("Arial", current_font_size))
Fonts_menu.add_command(label="Times New Roman", command=lambda: set_font("Times New Roman", current_font_size))
Fonts_menu.add_command(label="Courier New", command=lambda: set_font("Courier New", current_font_size))
Fonts_menu.add_command(label="Verdana", command=lambda: set_font("Verdana", current_font_size))
Fonts_menu.add_command(label="Georgia", command=lambda: set_font("Georgia", current_font_size))



# Zoom Menu (Changes the GUI Zoom Level)
Zoom_menu = Menu(my_menu)
my_menu.add_cascade(label="Zoom", menu=Zoom_menu)
Zoom_menu.add_command(label="Zoom In", command=zoom_in)
Zoom_menu.add_command(label="Zoom Out", command=zoom_out) 



# Initialize the current font size and font name
current_font_size = 55
current_font = "Arial" 







#Main menu widgets
def tab_main_menu_widgets():
    global label1, button_Quiz, button_Lessons
    label1 = Label(root, text="Recognizing shapes", font=("Arial", 50))
    label1.grid(column=3, row=0, columnspan = 12)    

    button_Lessons = Button(root, text="Lessons", font=("Arial", 25),command = tab_Lesson_menu ) 
    button_Lessons.grid(column=5, row =2, columnspan= 4)  
           
    button_Quiz = Button(root, text="Quiz!", font=("Arial", 25), command=tab_Quiz_menu) 
    button_Quiz.grid(column=9, row=2, columnspan = 4)   





#Trangles lesson part2 
def Triangle_info_part_2(): 
             global Triangle_text_frame2, button_previousinfo_triangles, Info_label2
             Triangle_text_frame.destroy()
             label_placeholder1.destroy()

             label_placeholder2 = Label(root, text="Isosceles triangle", font =("Arial", 50)) 
             label_placeholder2. grid(row=2, column =3, columnspan=12) 

             Triangle_text_frame2 = ScrolledFrame(root, height=700, width=800) 
             Triangle_text_frame2.grid(row=4, column=3, columnspan = 12, rowspan =10) 

             Info_label2 = Label(Triangle_text_frame2, text = Triangles2 , font=("Arial", 30), wraplength=770)
             Info_label2.grid(row=0, column=0)  
             
             def Triangleback(): 
                   button_previousinfo_triangles.destroy() 
                   Triangle_text_frame2.destroy()  
                   label_placeholder2.destroy()
                   Triangle_lesson_info()

             button_previousinfo_triangles = Button(root, text=("<---"), font=("Arial", 30),command = Triangleback) 
             button_previousinfo_triangles.grid(row=3, column=1)  








#Triangles lesson 
def Triangle_lesson_info(): 
       global Triangle_text_frame, label_placeholder1
       label_2.destroy() 
       button_triangles.destroy() 
       button_non_polygon.destroy() 
       button_quads.destroy() 
       button_polygons.destroy() 
       backb1.destroy()


       # These labels are place holders for the  actual images 
       label_placeholder1 = Label(root, text="Equilateral triangle", font =("Arial", 50)) 
       label_placeholder1. grid(row=2, column =3, columnspan=12) 

       #Lesson information scorallable frame
       Triangle_text_frame = ScrolledFrame(root, height=700, width=800) 
       Triangle_text_frame.grid(row=4, column=3, columnspan = 12, rowspan =10) 

       Info_label_Triangle = Label(Triangle_text_frame, text = Triangles1 , font=("Arial", 40), wraplength=770)
       Info_label_Triangle.grid(row=0, column=0)   



       #Next and previous button to switch between lesson information 
       button_nextinfo_triangles = Button(root, text=("--->"), font=("Arial", 30), command = Triangle_info_part_2)
       button_nextinfo_triangles.grid(row=3, column=16)  

       def back_T_lesson():
              Triangle_text_frame.destroy()

              tab_Lesson_menu()


       exit_lesson_button = Button(root, text="Exit", font=("Arial", 25), command=back_T_lesson) 
       exit_lesson_button.grid(column=0, row =0, columnspan = 4)  
        






def quads_info_part_2(): 
             Square_text_frame.destroy()   
             label_placeholder_sq.destroy()

             label_placeholder_sq2 = Label(root, text="parralellogram", font =("Arial", 50)) 
             label_placeholder_sq2. grid(row=2, column =3, columnspan=12) 

             Square_text_frame2 = ScrolledFrame(root, height=700, width=800) 
             Square_text_frame2.grid(row=4, column=3, columnspan = 12, rowspan =10) 

             Info_label2 = Label(Square_text_frame2, text = Square2 , font=("Arial", 40), wraplength=770)
             Info_label2.grid(row=0, column=0)  
             
             def squareback(): 
                   button_previousinfo_square.destroy() 
                   Square_text_frame2.destroy()  
                   label_placeholder_sq2.destroy()
                   quads_lesson_info()

             button_previousinfo_square = Button(root, text=("<---"), font=("Arial", 30),command = squareback) 
             button_previousinfo_square.grid(row=3, column=1) 







def quads_lesson_info(): 
    global Square_text_frame, label_placeholder_sq
    label_2.destroy() 
    button_triangles.destroy() 
    button_non_polygon.destroy() 
    button_quads.destroy() 
    button_polygons.destroy() 
    backb1.destroy()


    # These labels are place holders for the  actual images 
    label_placeholder_sq = Label(root, text="Square", font =("Arial", 50)) 
    label_placeholder_sq. grid(row=2, column =3, columnspan=12) 

    #Lesson information scorallable frame
    Square_text_frame = ScrolledFrame(root, height=700, width=800) 
    Square_text_frame.grid(row=4, column=3, columnspan = 12, rowspan =10) 

    Info_label_Square = Label(Square_text_frame, text = Square1 , font=("Arial", 40), wraplength=770)
    Info_label_Square.grid(row=0, column=0)   


            
    #Next and previous button to switch between lesson information 
    button_nextinfo_quads = Button(root, text=("--->"), font=("Arial", 30), command = quads_info_part_2)
    button_nextinfo_quads.grid(row=3, column=16)  




    exit_lesson_buttonq = Button(root, text="Exit", font=("Arial", 25)) 
    exit_lesson_buttonq.grid(column=0, row =0, columnspan = 4)  
        




def Polygons_lesson_info(): 
    pass 

def non_Polygons_lesson_info(): 
    pass
                    
               









#Lessons_page
def tab_Lesson_menu():
    global label_2, button_triangles, button_quads, button_non_polygon, button_polygons, backb1
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
    button_triangles = Button(root, text="Triangles", font=("Arial", 25), command = Triangle_lesson_info) 
    button_triangles.grid(column=4, row =1, columnspan= 4) 

    button_quads = Button(root, text="Quadrilaterals", font=("Arial", 25), command = quads_lesson_info) 
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





#Quiz 1 exam page
def tabquiz1(): 
    label_3rdpage.destroy() 
    backb2.destroy() 
    button_q1.destroy()
    

   # Quiz class
    class QuizApp:
        def __init__(Quiz, root):
            Quiz.root = root
            Quiz.question_index = 0
            Quiz.score = 0

            Quiz.questions = [
                "Which shape has three sides?",
                "Which shape has four equal sides?",
                "Which shape has five sides?",
            ]

            Quiz.options = [
                ["Square", "Triangle", "Pentagon", "Circle"],
                ["Rectangle", "Square", "Triangle", "Pentagon"],
                ["Triangle", "Square", "Pentagon", "Hexagon"],
            ]

            Quiz.correct_answers = ["Triangle", "Square", "Pentagon"]

            Quiz.setup_quiz_ui()

        def setup_quiz_ui(Quiz):
            Quiz.label_question = Label(Quiz.root, text=Quiz.questions[Quiz.question_index], font=("Arial", 25))
            Quiz.label_question.grid(row=2, column=3, columnspan=12)

            Quiz.var_option = StringVar()
            Quiz.var_option.set(None)

            Quiz.radio_buttons = []
            for i in range(4):
                radio_btn = Radiobutton(
                    Quiz.root, text=Quiz.options[Quiz.question_index][i],
                    variable=Quiz.var_option, value=Quiz.options[Quiz.question_index][i], font=("Arial", 20)
                )
                radio_btn.grid(row=4 + i, column=3, columnspan=12, sticky=W)
                Quiz.radio_buttons.append(radio_btn)

            Quiz.button_next = Button(Quiz.root, text="Next", font=("Arial", 20), command=Quiz.next_question)
            Quiz.button_next.grid(row=8, column=10)

        def next_question(Quiz):
            if Quiz.var_option.get() == Quiz.correct_answers[Quiz.question_index]:
                Quiz.score += 1

            Quiz.question_index += 1

            if Quiz.question_index < len(Quiz.questions):
                Quiz.update_quiz_ui()
            else:
                Quiz.display_result()

        def update_quiz_ui(Quiz):
            Quiz.label_question.config(text=Quiz.questions[Quiz.question_index])
            Quiz.var_option.set(None)
            for i, radio_btn in enumerate(Quiz.radio_buttons):
                radio_btn.config(text=Quiz.options[Quiz.question_index][i])

        def display_result(Quiz):
            Quiz.label_question.destroy()
            for radio_btn in Quiz.radio_buttons:
                radio_btn.destroy()
            Quiz.button_next.destroy()

            score_label = Label(Quiz.root, text=f"Your score is: {Quiz.score} out of {len(Quiz.questions)}", font=("Arial", 30))
            score_label.grid(row=2, column=3, columnspan=12)
            
            Quiz.button_back = Button(Quiz.root, text="<---", font=("Arial", 30), command=Quiz.back_to_main)
            Quiz.button_back.grid(row=3, column=1)

        def back_to_main(Quiz):
            for widget in Quiz.root.winfo_children():
                widget.destroy()
            tab_main_menu_widgets()


    
    

#main menu
def tab_main_menu(): 
    tab_main_menu_widgets()
tab_main_menu()



root.mainloop() 