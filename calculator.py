from tkinter import *
import math
import keyboard

def calculator():


    # Intialising the window
    window = Tk()
    window.title("Calculator")
    window.configure(bg= "white") #Default light mode
    window_height = 400
    window_width = 370
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    window.resizable(False, False)
    
    
    global numbers, decimal_counter, decimal_press
    numbers = 0
    numbers = int(numbers)
    decimal_press = False
    decimal_counter = 0
    # Entry box for displaying outputs
   # Text widget for displaying outputs (read-only)
    output_text = Text(window, width=30, height = 5, state="disabled")  # Set the desired width and height
    output_text.grid(row=0, column=0, columnspan=4,sticky="w")  # sticky="w" aligns the entry to the west (left)


    # Function to update the output text
    def update_output(value):
        output_text.config(state=NORMAL)
        output_text.delete(1.0, END)
        output_text.insert(END, str(value))
        output_text.config(state="disabled")

    

    
    def input_event(number: float, sign: bool, decimal: bool, decimal_pressed: bool):
        global numbers, decimal_counter, decimal_press
        if (sign):
            numbers *= -1
        elif (decimal):
            if (decimal_counter == 0):
                decimal_counter += 1
                decimal_press = True
                numbers = float(numbers)

        elif (decimal_pressed):       
            
          
            result = number / 10 ** decimal_counter
            decimal_counter += 1
           
            numbers += result
        else:
            numbers = numbers * (10) + number
            
     
        update_output(numbers)      
    def on_key_event(e):
       
        if (e.name == '1' or e.name == '2' or e.name == '3' or e.name == '4' or e.name == '5' or e.name == '6' or e.name == '7' or e.name == '8' or e.name == '9' or e.name == '0') and e.event_type == keyboard.KEY_UP:
            input_event(int(e.name), False, False, decimal_press)
        elif (e.name == '.'  or e.name == 'decimal') and e.event_type == keyboard.KEY_UP:
            input_event(0, False, True, decimal_press)

    # Hook for key events
    keyboard.hook(on_key_event)          

    #Establishing the menu bar and its functionality
    def dark_mode():
        #Making the calculator dark mode
        
        window.configure(bg="#333333")
         
        for i, button_text in enumerate(numbers_and_basic_properties):
            row = i // 3
            col = i % 3
            if (i == 9):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda: input_event(0, True, False, decimal_press))
            elif (i == 10):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda: input_event(0, False, False, decimal_press))
            elif (i == 11):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda: input_event(0, False, True, decimal_press))
            elif ((9 - i) % 3 == 1):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: input_event(11 - i, False, False, decimal_press))
            elif ((9 - i) % 3 == 0):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: input_event(7 - i, False, False, decimal_press))
            else:
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: input_event(9 - i, False, False, decimal_press))
            button.configure(bg="#333333")
            button.grid(row=row, column=col)
    def light_mode():
        #Making the calculator light mode
        window.configure(bg = "white")
        for i, button_text in enumerate(numbers_and_basic_properties):
            row = i // 3
            col = i % 3
            if (i == 9):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda: input_event(0, True, False, decimal_press))
            elif (i == 10):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda: input_event(0, False, False, decimal_press))
            elif (i == 11):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda: input_event(0, False, True, decimal_press))
            elif ((9 - i) % 3 == 1):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: input_event(11 - i, False, False, decimal_press))
            elif ((9 - i) % 3 == 0):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: input_event(7 - i, False, False, decimal_press))
            else:
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: input_event(9 - i, False, False, decimal_press))
            button.configure(bg="white")
            button.grid(row=row, column=col)

   
    
    menubar = Menu(window, background = "blue", fg="pink")
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu = filemenu)
    filemenu.add_command(label="Guide to use the calculator")
    filemenu.add_separator()
    filemenu.add_command(label= "Dark Mode", command = dark_mode)
    filemenu.add_command(label= "Light Mode", command = light_mode)
    filemenu.add_separator()
    filemenu.add_command(label= "Restart")
    

    
    menubar.add_cascade(label = "Exit", command = window.quit)
    # filemenu.add_command(label="Exit", menu = filemenu, command=window.quit)
    
    window.config(menu=menubar)


    #Creating the numbers of the calculator
    numbers_and_basic_properties = [
        "  7  ", "  8  ", "  9  ",
        "  4  ", "  5  ", "  6  ",
        "  1  ", "  2  ", "  3  ",
        "+/-", "  0  ", "  .   "
    ]
    
    for i, button_text in enumerate(numbers_and_basic_properties):
        row = i // 3 
        col = i % 3
        
        
        if (i == 9):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda: input_event(0, True, False, decimal_press))
        elif (i == 10):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda: input_event(0, False, False, decimal_press))
        elif (i == 11):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda: input_event(0, False, True, decimal_press))
        elif ((9 - i) % 3 == 1):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: input_event(11 - i, False, False, decimal_press))
        elif ((9 - i) % 3 == 0):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: input_event(7 - i, False, False, decimal_press))
        else:
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: input_event(9 - i, False, False, decimal_press))
                
        button.grid(row= row + 1, column=col)

    basic_operations = [
         "DEL", "AC", "  +  ", "  -  ", "  x  ", "  /  ", "ANS", " = "
    ]
    for i, button_text in enumerate(basic_operations):
        row = i // 2 
        col = i % 2
        button = Button(window, text=button_text, padx=20, pady=20)
        button.grid(row= row + 1, column=col + 3)
    
    
    window.mainloop()












if __name__ == "__main__":
    calculator()