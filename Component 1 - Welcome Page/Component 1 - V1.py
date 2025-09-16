"""
Component 1 - V1
"""

import tkinter as tk

root = tk.Tk()

#functions for welcome page widgets
def quit():
    root.destroy() #code for close program button

def to_map():
    root.destroy() #code for proceeding to the interactive map
"""placeholder"""

logo = tk.PhotoImage(file = "Logofinal.png") #logo import

logo = logo.subsample(2) 

Button_colour =  "#2cdfdd"

Background_colour = "#f3f1eb"

#window 
root.title("Entry Box")
root.resizable(0,0)
root.geometry("1200x800")
root.configure(bg= Background_colour)


#welcome page widgets
logo_label = tk.Label(root, image=logo, bg= Background_colour)
logo_label.pack(side="top", ipady=40, padx=10, pady=40, expand=True, fill="both" )

button_continue = tk.Button(root, text = "Continue".title(), bg = Button_colour, fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = to_map)
button_continue.pack(side="right" , ipady=10, padx = 10, pady = 10)
    
button_quit = tk.Button(root, text = "Quit", bg = Button_colour, fg = "white",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = quit)
button_quit.pack(side="top", ipady=10, padx = 10, pady = 10)



root.mainloop()