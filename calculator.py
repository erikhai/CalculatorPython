from tkinter import *



def calculator():


    # Intialising the window
    window = Tk()
    window.title("Calculator")
    window.configure(bg= "white") #Deafult light mode
    window_height = 400
    window_width = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    window.resizable(False, False)

    #Establishing the menu bar and its functionality
    def dark_mode():
        #Making the calculator dark mode
        
        window.configure(bg="#333333")
         
        for i, button_text in enumerate(numbers_and_basic_properties):
            row = i // 3
            col = i % 3
            if (i == 9):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button +/- pressed."))
            elif (i == 10):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button 0 pressed."))
            elif (i == 11):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button . pressed."))
            elif ((9 - i) % 3 == 1):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button {11 - i} pressed."))
            elif ((9 - i) % 3 == 0):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button {7 - i} pressed."))
            else:
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "white", command=lambda i=i: print(f"Button {9 - i} pressed."))
            button.configure(bg="#333333")
            button.grid(row=row, column=col)
    def light_mode():
        #Making the calculator light mode
        window.configure(bg = "white")
        for i, button_text in enumerate(numbers_and_basic_properties):
            row = i // 3
            col = i % 3
            if (i == 9):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button +/- pressed."))
            elif (i == 10):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button 0 pressed."))
            elif (i == 11):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button . pressed."))
            elif ((9 - i) % 3 == 1):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button {11 - i} pressed."))
            elif ((9 - i) % 3 == 0):
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button {7 - i} pressed."))
            else:
                button = Button(window, text=button_text, padx=20, pady=20, bg = "white", fg = "black", command=lambda i=i: print(f"Button {9 - i} pressed."))
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
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button +/- pressed."))
        elif (i == 10):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button 0 pressed."))
        elif (i == 11):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button . pressed."))
        elif ((9 - i) % 3 == 1):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button {11 - i} pressed."))
        elif ((9 - i) % 3 == 0):
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button {7 - i} pressed."))
        else:
            button = Button(window, text=button_text, padx=20, pady=20, command=lambda i=i: print(f"Button {9 - i} pressed."))
            
        button.grid(row=row, column=col)

    window.mainloop()












if __name__ == "__main__":
    calculator()