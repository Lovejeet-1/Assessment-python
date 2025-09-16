"""""""""""""""
Component 1 - V2
"""""""""""""""

welcomebuttons_colour = bg = "#2cdfdd"

welcomebackground_colour = "#f3f1eb"

import tkinter as tk

class WelcomePage():
    def __init__ (self):
        self.root=tk.Tk()
        #window 
        self.root.title("Entry Box")
        self.root.resizable(0,0)
        self.root.geometry("1200x800")
        self.root.configure(bg= welcomebackground_colour)

        self.create_widgets_welcome()

        self.root.mainloop()

    def create_widgets_welcome(self):
        
        #images
        self.logo = tk.PhotoImage(file = "Logofinal.png") #logo import

        self.logo = self.logo.subsample(2) 

        #welcome page widgets
        logo_label = tk.Label(self.root, image=self.logo, bg= welcomebackground_colour)
        logo_label.pack(side="top", ipady=40, padx=10, pady=40, expand=True, fill="both" )

        button_continue = tk.Button(self.root, text = "Continue".title(), bg = welcomebuttons_colour, fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = quit)
        button_continue.pack(side="right" , ipady=10, padx = 10, pady = 10)
    
        button_quit = tk.Button(self.root, text = "Quit", bg = welcomebuttons_colour, fg = "white",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = quit)
        button_quit.pack(side="top", ipady=10, padx = 10, pady = 10)

    #functions for welcome page widgets
    def quit(self):
        self.root.destroy() #code for close program button

    def to_map(self):
        self.root.destroy() #code for proceeding to the interactive map
        MapPage()


"""""""""""""""
Component 2 - V3
"""""""""""""""

import tkinter as tk

mapbackground_colour = "#d4c29a"

class MapPage:
    def __init__(self):

        #Window
        self.root = tk.Tk()
        self.root.title("Map Page")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")
        self.root.configure(bg ="white")

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        
        #upload and load images
        self.map = tk.PhotoImage(file = "Global_Map.png")

        self.red_button = tk.PhotoImage(file = "red_button.png")
        self.red_button = self.red_button.subsample(4)

        #setup map
        map_label = tk.Label(self.root, image= self.map, bg = mapbackground_colour, borderwidth = 0, )
        map_label.pack(expand = True, fill="both", side = "top")

        #Frame for buttons for all the different cruise ship lines offered
        button_frame = tk.Frame(self.root, bg = mapbackground_colour)
        button_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #6 buttons for all the different options
        button1 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button1.pack(side="left", padx=50, pady=5)

        button2 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button2.pack(side="left", padx=50, pady=5)

        button3 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button3.pack(side="left", padx=50, pady=5)

        button4 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button4.pack(side="left", padx=50, pady=5)

        button5 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button5.pack(side="left", padx=50, pady=5)

        button6 = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0)
        button6.pack(side="left", padx=50, pady=5)

        #back button frame
        backbutton_frame = tk.Frame(self.root, bg = mapbackground_colour)
        backbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #back to welcome button
        button_back = tk.Button(backbutton_frame, text = "Back".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.back_to_welcome)
        button_back.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)
   

    def back_to_welcome(self):
        self.root.destroy() #placeholder, add welcomepage()

    def to_customerdetails(self):
        self.root.destroy()

if __name__ == "__main__":
        WelcomePage()



    