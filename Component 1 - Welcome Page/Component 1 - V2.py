"""""""""""""""
Component 1 - V2
"""""""""""""""
import tkinter as tk

welcomebuttons_colour = bg = "#2cdfdd"

welcomebackground_colour = "#f3f1eb"

class WelcomePage():
    def __init__ (self):
        #window 
        self.root=tk.Tk()
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


if __name__ == "__main__":
    WelcomePage()




