"""""""""""""""
Component 2 - V2
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


    def NorthAmerica_Cruise_Popup(self): #method to display Europe Cruises Popup
        
        #Window (for NA popup)

        NorthAmerica_Cruise_Popup = tk.Toplevel(self.root)
        self.root.title("North America Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

        #import image
        self.NA_image = tk.PhotoImage(file = "NACruiseInfo.png") 

        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.NA_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)

    def SouthAmerica_Cruise_Popup(self): 
        
        SouthAmerica_Cruise_Popup = tk.Toplevel(self.root)
        self.root.title("South America Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

        #import image
        self.SA_image = tk.PhotoImage(file = "SACruiseInfo.png") 

        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.SA_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)


    def Europe_Cruise_Popup(self): #method to display Europe Cruises Popup

        #Window (for Europe popup)
        Europe_popup = tk.Toplevel(self.root)
        self.root.title("Europe Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

       
        #import image
        self.EU_image = tk.PhotoImage(file = "EuropeCruiseInfo.png") 
        self.EU_image = self.EU_image.subsample(4)

        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.EU_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)
    
    def Saudi_Cruise_Popup(self): 
        
        Europe_Cruise_Popup = tk.Toplevel(self.root)
        self.root.title("Saudi Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

        #import image
        self.Saudi_image = tk.PhotoImage(file = "Europe1.jpg") #placeholder edit with created image from canva later

        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.Saudi_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)


    def Asia_Cruise_Popup(self): 
        

        Europe_Cruise_Popup = tk.Toplevel(self.root)
        self.root.title("Asia Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

        #import image
        self.Asia_image = tk.PhotoImage(file = "AsiaCruiseInfo") 

        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.Asia_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)


    def Oceania_Cruise_Popup(self): 
        

        Europe_Cruise_Popup = tk.Toplevel(self.root)
        self.root.title("Oceania Cruise")
        self.root.resizable(False, False)
        self.root.geometry("1400x1000")

        #import image
        self.OCE_image = tk.PhotoImage(file = "Europe1.jpg") #placeholder edit with created image from canva later
 
        #label for image 
        map_label = tk.Label(self.root, bg = "black", borderwidth = 0, image = self.OCE_image )
        map_label.pack(expand = True, fill="both")

        #Frame for booking button
        bookbutton_frame = tk.Frame(self.root, bg = "red")
        bookbutton_frame.pack(pady=0, padx=0, expand = True, fill = "both")

        #booking button
        button_book = tk.Button(bookbutton_frame, text = "Book".title(), bg = "red", fg = "White",
                     font = ("Times New Roman", 35, "bold"), width = 20, command = self.to_customerdetails)
        button_book.pack(side="bottom" , ipady=10, padx = 10, pady = 10,)


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
        buttonNA = tk.Button(button_frame, text="North America", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command= self.NorthAmerica_Cruise_Popup)
        buttonNA.pack(side="left", padx=50, pady=5)

        buttonSA = tk.Button(button_frame, text="South America", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command= self.SouthAmerica_Cruise_Popup)
        buttonSA.pack(side="left", padx=50, pady=5)

        buttonEU = tk.Button(button_frame, text="Europe", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command = self.selfdestroy)
        buttonEU.pack(side="left", padx=50, pady=5)

        buttonSAUDI = tk.Button(button_frame, text="Saudi", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command= self.Saudi_Cruise_Popup)
        buttonSAUDI.pack(side="left", padx=50, pady=5)

        buttonASIA = tk.Button(button_frame, text="Asia", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command= self.Asia_Cruise_Popup)
        buttonASIA.pack(side="left", padx=50, pady=5)

        buttonOCE = tk.Button(button_frame, text="Oceania", image = self.red_button, bg = mapbackground_colour, borderwidth=0, command= self.Oceania_Cruise_Popup)
        buttonOCE.pack(side="left", padx=50, pady=5)

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
    MapPage()
