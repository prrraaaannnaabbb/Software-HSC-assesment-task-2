from tkinter import *
import customtkinter
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import ImageTk, Image
from Triangles_data1 import Triangles1
from Triangles_data2 import Triangles2
from Square_data1 import Square1
from Square_data2 import Square2
from polygon_data1 import polygon1
from polygon_data2 import polygon2
from non_polygon_data1 import nonpoly1 
from non_polygon_data2 import nonpoly2 



# Setup
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()


app_width = 600
app_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

root.title("SDD Task 2")
root.minsize(600, 600)

# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(12)), weight=10, uniform="a")



def inclusivity_features(): 
    # Inclusivity features
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


    # Theme Change Functions
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
        

    # Menu Bar Options (Inclusivity Features)
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # File Menu Item (Quits the program)
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="Options", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    # Themes Menu
    Themes_menu = Menu(my_menu)
    my_menu.add_cascade(label="Themes", menu=Themes_menu)
    Themes_menu.add_command(label="Dark", command=dark_theme)
    Themes_menu.add_command(label="Light", command=light_theme)
    Themes_menu.add_command(label="Chestnut", command=chestnut_theme)
    Themes_menu.add_command(label="Navy", command=navy_theme)
    Themes_menu.add_command(label="Beige", command=beige_theme)
    Themes_menu.add_command(label="Burgundy", command=burgundy_theme)
    Themes_menu.add_command(label="Light Aqua", command=light_aqua_theme)
    Themes_menu.add_command(label="Botanical", command=botanical_theme)
    Themes_menu.add_command(label="Honey", command=honey_theme)


    # Font Change Function
    def set_font(new_font, new_font_size):
        font_tuple = (new_font, new_font_size)
        for widget in root.winfo_children():
            widget.config(font=font_tuple)
        root.update()


    def zoom_in():
        global current_font_size
        current_font_size = 35
        current_font_size += 20
        set_font(current_font, current_font_size)

    def zoom_out():
        global current_font_size
        current_font_size = max(current_font_size - 10, 1)
        set_font(current_font, current_font_size)

    # Fonts Menu
    Fonts_menu = Menu(my_menu)
    my_menu.add_cascade(label="Fonts", menu=Fonts_menu)
    Fonts_menu.add_command(label="Helvetica", command=lambda: set_font("Helvetica", current_font_size))
    Fonts_menu.add_command(label="Arial", command=lambda: set_font("Arial", current_font_size))
    Fonts_menu.add_command(label="Times New Roman", command=lambda: set_font("Times New Roman", current_font_size))
    Fonts_menu.add_command(label="Courier New", command=lambda: set_font("Courier New", current_font_size))
    Fonts_menu.add_command(label="Verdana", command=lambda: set_font("Verdana", current_font_size))
    Fonts_menu.add_command(label="Georgia", command=lambda: set_font("Georgia", current_font_size))

    # Zoom Menu
    Zoom_menu = Menu(my_menu)
    my_menu.add_cascade(label="Zoom", menu=Zoom_menu)
    Zoom_menu.add_command(label="Zoom In", command=zoom_in)
    Zoom_menu.add_command(label="Zoom Out", command=zoom_out)

    # Initialize the current font size and font name
    current_font_size = 35
    current_font = "Arial"
inclusivity_features()




# Main menu widgets
def tab_main_menu_widgets():
    global label1, button_Quiz, button_Lessons
    label1 = Label(root, text="Recognizing Shapes", font=("Arial", 50))
    label1.grid(column=3, row=0, columnspan=12)

    button_Lessons = Button(root, text="Lessons", font=("Arial", 25), command=tab_Lesson_menu)
    button_Lessons.grid(column=5, row=2, columnspan=4)

    button_Quiz = Button(root, text="Quiz!", font=("Arial", 25), command=tab_Quiz_menu)
    button_Quiz.grid(column=9, row=2, columnspan=4) 




# Shapes menu
def Shapes_menu():
    
    global label_shapes_page, button_triangles, button_quads, button_non_polygon, button_polygon, backb1
    for widget in root.winfo_children():
        widget.destroy()
    
    inclusivity_features()

    label_shapes_page = Label(root, text="Lessons", font=("Arial", 50))
    label_shapes_page.grid(column=2, row=0, columnspan=13)

    button_triangles = Button(root, text="Triangles", font=("Arial", 25), command=Triangle_lesson_info)
    button_triangles.grid(row=3, column=4, columnspan=3)

    button_quads = Button(root, text="Quadrilateral", font=("Arial", 25), command=Quad_lesson_info)
    button_quads.grid(row=3, column=9, columnspan=3)

    button_polygon = Button(root, text="Polygons", font=("Arial", 25), command =polygon_lesson_info)
    button_polygon.grid(row=5, column=4, columnspan=3)

    button_non_polygon = Button(root, text="Non-Polygon", font=("Arial", 25), command=non_polygon_lesson_info)
    button_non_polygon.grid(row=5, column=9, columnspan=3)

    def back_to_main():
        for widget in root.winfo_children():
            widget.destroy()
        inclusivity_features()
        tab_main_menu_widgets()

    backb1 = Button(root, text="back", font=("Arial", 30), command=back_to_main)
    backb1.grid(row=1, column=1, columnspan=2)



# Triangles lesson
def Triangle_lesson_info():
    global Triangle_text_frame, label_placeholder1
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder1 = Label(root, text="Triangles", font=("Arial", 50))
    label_placeholder1.grid(row=2, column=3, columnspan=12)


    Triangle_text_frame = ScrolledFrame(root, height=700, width=800)
    Triangle_text_frame.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label_Triangle = Label(Triangle_text_frame, text=Triangles1, font=("Arial", 25), wraplength=770)
    Info_label_Triangle.grid(row=0, column=0)

    button_nextinfo_triangles = Button(root, text="--->", font=("Arial", 30), command=Triangle_info_part_2)
    button_nextinfo_triangles.grid(row=3, column=16)

    def back_to_shape_menu():
        for widget in root.winfo_children():
            widget.destroy()
        Shapes_menu()

    button_back_shapes = Button(root, text="Back", font=("Arial", 30), command=back_to_shape_menu)
    button_back_shapes.grid(row=2, column=1, columnspan=2)



# Triangles lesson part 2
def Triangle_info_part_2():
    global Triangle_text_frame2, button_previousinfo_triangles, label_placeholder2
    for widget in root.winfo_children():
        widget.destroy() 

    inclusivity_features()

    label_placeholder2 = Label(root, text="Triangles", font=("Arial", 50))
    label_placeholder2.grid(row=2, column=3, columnspan=12)

    Triangle_text_frame2 = ScrolledFrame(root, height=700, width=800)
    Triangle_text_frame2.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label2 = Label(Triangle_text_frame2, text=Triangles2, font=("Arial", 25), wraplength=770)
    Info_label2.grid(row=0, column=0)

    def Triangleback():
        for widget in root.winfo_children():
            widget.destroy()
        Triangle_lesson_info()

    button_previousinfo_triangles = Button(root, text="<---", font=("Arial", 30), command=Triangleback)
    button_previousinfo_triangles.grid(row=3, column=1)



# Quads lesson
def Quad_lesson_info():
    global Quad_text_frame, label_placeholder3
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder3 = Label(root, text="Quadrilaterals", font=("Arial", 50))
    label_placeholder3.grid(row=2, column=3, columnspan=12)

    Quad_text_frame = ScrolledFrame(root, height=700, width=800)
    Quad_text_frame.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label_Quad = Label(Quad_text_frame, text=Square1, font=("Arial", 25), wraplength=770)
    Info_label_Quad.grid(row=0, column=0)

    button_nextinfo_quads = Button(root, text="--->", font=("Arial", 30), command=Quad_info_part_2)
    button_nextinfo_quads.grid(row=3, column=16)

    def back_to_shape_menu():
        for widget in root.winfo_children():
            widget.destroy()
            Shapes_menu()

    button_back_quads = Button(root, text="Back", font=("Arial", 30), command=back_to_shape_menu)
    button_back_quads.grid(row=2, column=1, columnspan=2) 


# Quads lesson part 2
def Quad_info_part_2():
    global Quad_text_frame2, button_previousinfo_quads, label_placeholder4
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder4 = Label(root, text="Quadrilaterals", font=("Arial", 50))
    label_placeholder4.grid(row=2, column=3, columnspan=12)

    Quad_text_frame2 = ScrolledFrame(root, height=700, width=800)
    Quad_text_frame2.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label2 = Label(Quad_text_frame2, text=Square2, font=("Arial", 25), wraplength=770)
    Info_label2.grid(row=0, column=0)

    def Quadback():
      for widget in root.winfo_children():
        widget.destroy()
        Quad_lesson_info()

    button_previousinfo_quads = Button(root, text="<---", font=("Arial", 30), command=Quadback)
    button_previousinfo_quads.grid(row=3, column=1)



def polygon_lesson_info():
    global polygon_text_frame, label_placeholder4
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder4 = Label(root, text="Polygons", font=("Arial", 50))
    label_placeholder4.grid(row=2, column=3, columnspan=12)

    polygon_text_frame = ScrolledFrame(root, height=700, width=800)
    polygon_text_frame.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label_polygon = Label(polygon_text_frame, text=polygon1, font=("Arial", 25), wraplength=770)
    Info_label_polygon.grid(row=0, column=0)

    button_nextinfo_polygon = Button(root, text="--->", font=("Arial", 30), command=polygon_info_part_2)
    button_nextinfo_polygon.grid(row=3, column=16)

    def back_to_shape_menu():
        for widget in root.winfo_children():
            widget.destroy()
            Shapes_menu()

    button_back_polygon = Button(root, text="Back", font=("Arial", 30), command=back_to_shape_menu)
    button_back_polygon.grid(row=2, column=1, columnspan=2)



def polygon_info_part_2():
    global polygon_text_frame2, button_previousinfo_polygons, label_placeholder5
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder5 = Label(root, text="Polygons", font=("Arial", 50))
    label_placeholder5.grid(row=2, column=3, columnspan=12)

    polygon_text_frame2 = ScrolledFrame(root, height=700, width=800)
    polygon_text_frame2.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label5 = Label(polygon_text_frame2, text=polygon2, font=("Arial", 25), wraplength=770)
    Info_label5.grid(row=0, column=0)

    def polygonback():
      for widget in root.winfo_children():
        widget.destroy()
        polygon_lesson_info()

    button_previousinfo_polygons = Button(root, text="<---", font=("Arial", 30), command=polygonback)
    button_previousinfo_polygons.grid(row=3, column=1)    



def non_polygon_lesson_info(): 
    global non_polygon_text_frame, label_placeholder6
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder6 = Label(root, text="Non-polygons", font=("Arial", 50))
    label_placeholder6.grid(row=2, column=3, columnspan=12)

    non_polygon_text_frame = ScrolledFrame(root, height=700, width=800)
    non_polygon_text_frame.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label_non_polygon = Label(non_polygon_text_frame, text=nonpoly1, font=("Arial", 25), wraplength=770)
    Info_label_non_polygon.grid(row=0, column=0)

    button_nextinfo_polygon = Button(root, text="--->", font=("Arial", 30), command=non_polygon_lesson_info2)
    button_nextinfo_polygon.grid(row=3, column=16)

    def non_poly_back():
        for widget in root.winfo_children():
            widget.destroy()
            Shapes_menu()

    button_back_non_polygon = Button(root, text="Back", font=("Arial", 30), command=non_poly_back)
    button_back_non_polygon.grid(row=2, column=1, columnspan=2)



def non_polygon_lesson_info2(): 
    global non_polygon_text_frame2, button_previousinfo_non_polygons, label_placeholder7
    for widget in root.winfo_children():
        widget.destroy()

    inclusivity_features()

    label_placeholder7 = Label(root, text="Non-polygons", font=("Arial", 50))
    label_placeholder7.grid(row=2, column=3, columnspan=12)

    non_polygon_text_frame2 = ScrolledFrame(root, height=700, width=800)
    non_polygon_text_frame2.grid(row=4, column=3, columnspan=12, rowspan=10)

    Info_label7 = Label(non_polygon_text_frame2, text=nonpoly2, font=("Arial", 25), wraplength=770)
    Info_label7.grid(row=0, column=0)

    def polygonback():
        for widget in root.winfo_children():
            widget.destroy()
        polygon_lesson_info()

    button_previousinfo_non_polygons = Button(root, text="<---", font=("Arial", 30), command=polygonback)
    button_previousinfo_non_polygons.grid(row=3, column=1)    


# Quiz code
class QuizApp:
    def __init__(Quiz, root):
        inclusivity_features()
        Quiz.root = root
        Quiz.question_index = 0
        Quiz.score = 0

        Quiz.questions = [
            "Which shape has three sides?",
            "Which shape has four equal sides?",
            "Which shape has five sides?",
            "Which triangles has only 2 equal sides?", 
            "what shape would have no straight lines but is 360 degrees?", 
            "Which shape is a polygon?", 
            "What is a non-polygon?",
            "Which shape is a non-polygon?", 
            "I am a shape that is enclosed with 3 straight defined as?",
            "Which shape is a Quadrilteral?"
        
        ]

        Quiz.options = [
            ["Square", "Triangle", "Pentagon", "Circle"],
            ["Square", "Circle", "Triangle", "Pentagon"],
            ["Triangle", "Square", "Pentagon", "Hexagon"],
            ["Scalene","Equilateral", "isosceles", "Rectangle"], 
            ["Square", "Decagon", "Circle", "Hexagon"], 
            ["Rectangle","Square", "Triangle", "All of the above"],
            [ "A four sided shape", "A three sided shape", "A shape that does not satisfy the criteria of a polygon","A shape the has 360 degrees with atleast 5 straight lines"],
            ["Rhombus", "Circle", "Triangle", "Polygon"],  
            ["Triangle", "Pentagon", "Oval", "Kite"], 
            ["Kite", "Rectangle", "Square", "All of the above"]

        ]

        Quiz.correct_answers = [
            "Triangle",
            "Square", 
            "Pentagon",
            "isosceles", 
            "Circle",
            "All of the above",
            "A shape that does not satisfy the criteria of a polygon",
            "Circle",
            "Triangle",
            "All of the above"
            ]

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

        Quiz.button_next = Button(Quiz.root, text="Next", font=("Arial", 25), command=Quiz.next_question)
        Quiz.button_next.grid(row=5, column=12, columnspan = 2)

        Quiz.Exit_button =  Button(Quiz.root, text="Exit", font=("Arial", 25), command=Quiz.Exit) 
        Quiz.Exit_button.grid(row=1, column=1, columnspan=2) 

    def Exit(Quiz):
        for widget in Quiz.root.winfo_children():
            widget.destroy()
        inclusivity_features()
        tab_main_menu_widgets()


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




def tab_Lesson_menu():
    for widget in root.winfo_children():
        widget.destroy()
    Shapes_menu()


def tab_Quiz_menu():
    for widget in root.winfo_children():
        widget.destroy()
    quiz_app = QuizApp(root)


tab_main_menu_widgets()

root.mainloop() 








