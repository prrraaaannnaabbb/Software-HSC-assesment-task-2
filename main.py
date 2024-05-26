from tkinter import *
import customtkinter
from ttkbootstrap.scrolled import ScrolledFrame
from Triangles_data1 import Triangles1
from Triangles_data2 import Triangles2
from Square_data1 import Square1 
from Square_data2 import Square2 




# Setup
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()

root.title("SDD Task 2")
root.geometry("600x600")
root.minsize(600, 600)


# Define grid
root.columnconfigure(list(range(18)), weight=10, uniform="a")
root.rowconfigure(list(range(12)), weight=10, uniform="a")




#inclusivity features 



#Menu Bar Options (Inclusivity Features)
my_menu = Menu(root)
root.config(menu=my_menu) 

    #File Menu Item (Quits the program)
file_menu = Menu(my_menu) 
my_menu.add_cascade(label = "options", menu=file_menu) 
file_menu.add_command(label="Exit", command=root.quit) 



#The following functions are for the inclusivity features:
def beige_theme():
    root.config(bg="#F5E0C0")  # Change background color to beige using hexadecimal color code
    sum_label.config(bg="#EE9E8D", fg="black")  # Change sum_label colors
    first_term_label.config(bg="#F5E0C0", fg="black")
    common_difference_label.config(bg="#F5E0C0", fg="black")
    common_ratio_label.config(bg="#F5E0C0", fg="black")
    num_terms_label.config(bg="#F5E0C0", fg="black")
    arithmetic_radio.config(bg="#F5E0C0", fg="black")
    geometric_radio.config(bg="#F5E0C0", fg="black")
    first_term_entry.config(bg="#D9CCA2", fg="black")  # Using a different color for entry fields
    common_difference_entry.config(bg="#D9CCA2", fg="black")
    common_ratio_entry.config(bg="#D9CCA2", fg="black")
    num_terms_entry.config(bg="#D9CCA2", fg="black")
    calculate_button.config(bg="#BEEEA0", fg="black")  # Using a different color for the button
    clear_button.config(bg="#BEEEA0", fg="black")  # Adding color for the Clear button
    root.update()  # Update the GUI to reflect the color changes

def navy_theme():
    root.config(bg="#2C3E50")  # Change background color using hexadecimal color code
    sum_label.config(bg="#2C3E50", fg="white")  # Change sum_label colors
    first_term_label.config(bg="#2C3E50", fg="white")
    common_difference_label.config(bg="#2C3E50", fg="white")
    common_ratio_label.config(bg="#2C3E50", fg="white")
    num_terms_label.config(bg="#2C3E50", fg="white")
    arithmetic_radio.config(bg="#2C3E50", fg="white")
    geometric_radio.config(bg="#2C3E50", fg="white")
    first_term_entry.config(bg="#34495E", fg="white")  # Using a different color for entry fields
    common_difference_entry.config(bg="#34495E", fg="white")
    common_ratio_entry.config(bg="#34495E", fg="white")
    num_terms_entry.config(bg="#34495E", fg="white")
    calculate_button.config(bg="#E74C3C", fg="white")  # Using a different color for the button
    clear_button.config(bg="#E74C3C", fg="white")  # Adding color for the Clear button
    root.update()  # Update the GUI to reflect the color changes  

def burgundy_theme():
    root.config(bg="#800020")  # Background color 
    sum_label.config(bg="#672F25", fg="white")  # Adjust sum_label colors
    first_term_label.config(bg="#672F25", fg="white")
    common_difference_label.config(bg="#672F25", fg="white")
    common_ratio_label.config(bg="#672F25", fg="white")
    num_terms_label.config(bg="#672F25", fg="white")
    arithmetic_radio.config(bg="#672F25", fg="white")
    geometric_radio.config(bg="#672F25", fg="white")
    first_term_entry.config(bg="grey", fg="black")  # Using a different color for entry fields
    common_difference_entry.config(bg="grey", fg="black")
    common_ratio_entry.config(bg="grey", fg="black")
    num_terms_entry.config(bg="grey", fg="black")
    calculate_button.config(bg="#c4a747", fg="black")  # Using a different color for the button
    clear_button.config(bg="#c4a747", fg="black")  # Adding color for the Clear button
    root.update()  # Update the GUI to reflect the color changes 

def light_aqua_theme():
    root.config(bg="#A2C4C9")  # Background color inspired by 
    sum_label.config(bg="#A2C4C9", fg="black")  # Adjust sum_label colors
    first_term_label.config(bg="#A2C4C9", fg="black")
    common_difference_label.config(bg="#A2C4C9", fg="black")
    common_ratio_label.config(bg="#A2C4C9", fg="black")
    num_terms_label.config(bg="#A2C4C9", fg="black")
    arithmetic_radio.config(bg="#A2C4C9", fg="black")
    geometric_radio.config(bg="#A2C4C9", fg="black")
    first_term_entry.config(bg="grey", fg="black")  # Using a different color for entry fields
    common_difference_entry.config(bg="grey", fg="black")
    common_ratio_entry.config(bg="grey", fg="black")
    num_terms_entry.config(bg="grey", fg="black")
    calculate_button.config(bg="#8FCACF", fg="black")  # Using a different color for the button
    clear_button.config(bg="#8FCACF", fg="black")  # Adding color for the Clear button
    root.update()  # Update the GUI to reflect the color changes

def botanical_theme():
    root.config(bg="#446725")  # Background color inspired 
    sum_label.config(bg="#D0E2C8", fg="black")  # Adjust sum_label colors
    first_term_label.config(bg="#D0E2C8", fg="black")
    common_difference_label.config(bg="#D0E2C8", fg="black")
    common_ratio_label.config(bg="#D0E2C8", fg="black")
    num_terms_label.config(bg="#D0E2C8", fg="black")
    arithmetic_radio.config(bg="#D0E2C8", fg="black")
    geometric_radio.config(bg="#D0E2C8", fg="black")
    first_term_entry.config(bg="#F2F7EF", fg="black")  # Lighter color for entry fields
    common_difference_entry.config(bg="#F2F7EF", fg="black")
    common_ratio_entry.config(bg="#F2F7EF", fg="black")
    num_terms_entry.config(bg="#F2F7EF", fg="black")
    calculate_button.config(bg="#D198C0", fg="#4F2743")  # Using a different color for the button
    clear_button.config(bg="#D198C0", fg="#4F2743")  # Adding color for the Clear button
    root.update()  # Update the GUI to reflect the color changes 

def dark_theme():
    root.config(bg="#7F7C7E")  # Lighter background color
    sum_label.config(bg="#333333", fg="white")  # Darker color for sum_label
    first_term_label.config(bg="#333333", fg="white")  # Swapped label colors
    common_difference_label.config(bg="#333333", fg="white")
    common_ratio_label.config(bg="#333333", fg="white")
    num_terms_label.config(bg="#333333", fg="white")
    arithmetic_radio.config(bg="#333333", fg="white")
    geometric_radio.config(bg="#333333", fg="white")
    first_term_entry.config(bg="white", fg="black")  # Lighter color for entry fields
    common_difference_entry.config(bg="white", fg="black")
    common_ratio_entry.config(bg="white", fg="black")
    num_terms_entry.config(bg="white", fg="black")
    calculate_button.config(bg="#ADD8E6", fg="#7F7C7E")  # Light blue color for the Calculate button
    clear_button.config(bg="#ADD8E6", fg="#7F7C7E")  # Light blue color for the Clear button
    root.update()  # Update the GUI to reflect the color changes

def honey_theme():
    root.config(bg="#EECC64")  # Background color 
    sum_label.config(bg="#FDEB71", fg="black")  # Adjust sum_label colors
    first_term_label.config(bg="#FDEB71", fg="black")
    common_difference_label.config(bg="#FDEB71", fg="black")
    common_ratio_label.config(bg="#FDEB71", fg="black")
    num_terms_label.config(bg="#FDEB71", fg="black")
    arithmetic_radio.config(bg="#FDEB71", fg="black")
    geometric_radio.config(bg="#FDEB71", fg="black")
    first_term_entry.config(bg="#FFFCDB", fg="black")  # Light yellow for entry fields
    common_difference_entry.config(bg="#FFFCDB", fg="black")
    common_ratio_entry.config(bg="#FFFCDB", fg="black")
    num_terms_entry.config(bg="#FFFCDB", fg="black")
    calculate_button.config(bg="#FFB03B", fg="black")  # Warm orange color for the button
    clear_button.config(bg="#FFB03B", fg="black")  # Warm orange color for the Clear button
    root.update()  # Update the GUI to reflect the color changes 

def chestnut_theme():
    root.config(bg="#5E4420")  # Background color 
    sum_label.config(bg="#5E4420", fg="white")  # Adjust sum_label colors
    first_term_label.config(bg="#5E4420", fg="white")
    common_difference_label.config(bg="#5E4420", fg="white")
    common_ratio_label.config(bg="#5E4420", fg="white")
    num_terms_label.config(bg="#5E4420", fg="white")
    arithmetic_radio.config(bg="#5E4420", fg="white")
    geometric_radio.config(bg="#5E4420", fg="white")
    first_term_entry.config(bg="#8D6D49", fg="black")  # Darker brown for entry fields
    common_difference_entry.config(bg="#8D6D49", fg="black")
    common_ratio_entry.config(bg="#8D6D49", fg="black")
    num_terms_entry.config(bg="#8D6D49", fg="black")
    calculate_button.config(bg="#C98E3F", fg="white")  # Warm gold color for the button
    clear_button.config(bg="#C98E3F", fg="white")  # Warm gold color for the Clear button
    root.update()  # Update the GUI to reflect the color changes

def light_theme():
    root.config(bg="white")  # White background color
    sum_label.config(bg="white", fg="black")  # Adjust sum_label colors
    first_term_label.config(bg="white", fg="black")
    common_difference_label.config(bg="white", fg="black")
    common_ratio_label.config(bg="white", fg="black")
    num_terms_label.config(bg="white", fg="black")
    arithmetic_radio.config(bg="white", fg="black")
    geometric_radio.config(bg="white", fg="black")
    first_term_entry.config(bg="white", fg="black")  # Black text on white background for entry fields
    common_difference_entry.config(bg="white", fg="black")
    common_ratio_entry.config(bg="white", fg="black")
    num_terms_entry.config(bg="white", fg="black")
    calculate_button.config(bg="black", fg="white")  # Black button with white text
    clear_button.config(bg="black", fg="white")  # Black button with white text
    root.update()  # Update the GUI to reflect the color changes



















Themes_menu = Menu(my_menu) 
my_menu.add_cascade(label="Themes", menu = Themes_menu) 
Themes_menu.add_command(label="Dark") 
Themes_menu.add_separator()  
Themes_menu.add_command(label="Light") 
Themes_menu.add_separator()  
Themes_menu.add_command(label="Chestnut") 
Themes_menu.add_separator() 
Themes_menu.add_command(label="Navy")  
Themes_menu.add_separator()
Themes_menu.add_command(label="Beige")   
Themes_menu.add_separator()  
Themes_menu.add_command(label="Burgundy") 
Themes_menu.add_separator() 
Themes_menu.add_command(label="Light Aqua") 
Themes_menu.add_separator()  
Themes_menu.add_command(label="Botanical") 
Themes_menu.add_separator()  
Themes_menu.add_command(label="Honey")




# Font Change Function
def set_font(new_font, new_font_size):
    font_tuple = (new_font, new_font_size)

    # Update all the widgets with the new font
    label1.config(font=font_tuple)
    button_Lessons.config(font=font_tuple)
    button_Quiz.config(font=font_tuple)
    button_triangles.config(font=font_tuple)
    # num_terms_label.config(font=font_tuple)
    # arithmetic_radio.config(font=font_tuple)
    # geometric_radio.config(font=font_tuple)
    # first_term_entry.config(font=font_tuple)
    # common_difference_entry.config(font=font_tuple)
    # common_ratio_entry.config(font=font_tuple)
    # num_terms_entry.config(font=font_tuple)
    # calculate_button.config(font=font_tuple)
    # clear_button.config(font=font_tuple)


def zoom_in():
    global current_font_size
    current_font_size += 1
    set_font(current_font, current_font_size)

def zoom_out():
    global current_font_size
    current_font_size = max(current_font_size - 1, 1)
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
    label1 = Label(root, text="Recognizing shapes", font=("Arial", 60))
    label1.grid(column=3, row=0, columnspan = 12)    

    button_Lessons = Button(root, text="Lessons", font=("Arial", 40),command = tab_Lesson_menu ) 
    button_Lessons.grid(column=5, row =2, columnspan= 4)  
           
    button_Quiz = Button(root, text="Quiz!", font=("Arial", 40), command=tab_Quiz_menu) 
    button_Quiz.grid(column=9, row=2, columnspan = 4)   





#Trangles lesson part2 
def Triangle_info_part_2(): 
             global Triangle_text_frame2, button_previousinfo_triangles
             Triangle_text_frame.destroy()
             label_placeholder1.destroy()

             label_placeholder2 = Label(root, text="Isosceles triangle", font =("Arial", 50)) 
             label_placeholder2. grid(row=2, column =3, columnspan=12) 

             Triangle_text_frame2 = ScrolledFrame(root, height=700, width=800) 
             Triangle_text_frame2.grid(row=4, column=3, columnspan = 12, rowspan =10) 

             Info_label2 = Label(Triangle_text_frame2, text = Triangles2 , font=("Arial", 25), wraplength=770)
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

       Info_label_Triangle = Label(Triangle_text_frame, text = Triangles1 , font=("Arial", 25), wraplength=770)
       Info_label_Triangle.grid(row=0, column=0)   



       #Next and previous button to switch between lesson information 
       button_nextinfo_triangles = Button(root, text=("--->"), font=("Arial", 30), command = Triangle_info_part_2)
       button_nextinfo_triangles.grid(row=3, column=16)  

       def back_T_lesson():
              pass
            #   Triangle_text_frame.destroy()  
            #   button_nextinfo_triangles.destroy()   
            #   button_previousinfo_triangles.destroy()
            #   exit_lesson_button.destroy()
            #   tab_Lesson_menu()


       exit_lesson_button = Button(root, text="Exit", font=("Arial", 25), command=back_T_lesson) 
       exit_lesson_button.grid(column=0, row =0, columnspan = 4)  
        









def quads_info_part_2(): 
             Square_text_frame.destroy()   
             label_placeholder_sq.destroy()

             label_placeholder_sq2 = Label(root, text="parralellogram", font =("Arial", 50)) 
             label_placeholder_sq2. grid(row=2, column =3, columnspan=12) 

             Square_text_frame2 = ScrolledFrame(root, height=700, width=800) 
             Square_text_frame2.grid(row=4, column=3, columnspan = 12, rowspan =10) 

             Info_label2 = Label(Square_text_frame2, text = Square2 , font=("Arial", 30), wraplength=770)
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

    Info_label_Square = Label(Square_text_frame, text = Square1 , font=("Arial", 30), wraplength=770)
    Info_label_Square.grid(row=0, column=0)   


            
    #Next and previous button to switch between lesson information 
    button_nextinfo_quads = Button(root, text=("--->"), font=("Arial", 30), command = quads_info_part_2)
    button_nextinfo_quads.grid(row=3, column=16)  

    def back_T_lesson():
              pass
            #   Triangle_text_frame.destroy()  
            #   button_nextinfo_triangles.destroy()   
            #   button_previousinfo_triangles.destroy()
            #   exit_lesson_button.destroy()
            #   tab_Lesson_menu()


    exit_lesson_button = Button(root, text="Exit", font=("Arial", 25), command=back_T_lesson) 
    exit_lesson_button.grid(column=0, row =0, columnspan = 4)  
        
















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