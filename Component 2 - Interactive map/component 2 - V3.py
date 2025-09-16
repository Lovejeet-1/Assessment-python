"""""""""""""""
Component 2 - V3
"""""""""""""""

import tkinter as tk

class MapPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Map Page")
        self.root.resizable(False, False)
        self.root.geometry("1600x1000")
        self.root.configure(bg="white")

        self.mapbackground_colour = "#d4c29a"  
        self.create_widgets()
        self.root.mainloop()

    #function to create a popup with an image (subsampled & modal)
    def create_popup(self, title, image_path):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.resizable(False, False)
        popup.geometry("600x500")

        #popup modal
        popup.transient(self.root)  #keep popup on top of root
        popup.grab_set()  #disable interaction with main window

        # Load and store image
        self.current_image = tk.PhotoImage(file=image_path).subsample(3)

        #Image label
        map_label = tk.Label(popup, bg=self.mapbackground_colour, image=self.current_image)
        map_label.pack(expand=True, fill="both")

        #Frame for buttons (Book + Close)
        button_frame = tk.Frame(popup, bg=self.mapbackground_colour)
        button_frame.pack(expand=True, fill="both", pady=10)

        # Book button
        button_book = tk.Button(
            button_frame,
            text="Book",
            bg="red",
            fg="white",
            font=("Times New Roman", 25, "bold"),
            width=15,
            command=lambda: self.close_and_book(popup)
        )
        button_book.pack(side="left", expand=True, padx=10, pady=10)

        # Close button
        button_close = tk.Button(
            button_frame,
            text="Close",
            bg="red",
            fg="white",
            font=("Times New Roman", 25, "bold"),
            width=15,
            command=popup.destroy
        )
        button_close.pack(side="right", expand=True, padx=10, pady=10)

        #Wait until popup is closed before returning to main window
        popup.wait_window(popup)

    #method just calls create_popup with correct title/image
    def NorthAmerica_Cruise_Popup(self):
        self.create_popup("North America Cruise", "NACruiseInfo.png")

    def SouthAmerica_Cruise_Popup(self):
        self.create_popup("South America Cruise", "SACruiseInfo.png")

    def Europe_Cruise_Popup(self):
        self.create_popup("Europe Cruise", "EuropeCruiseInfo.png")

    def Saudi_Cruise_Popup(self):
        self.create_popup("Saudi Cruise", "SaudiCruiseInfo.png")

    def Asia_Cruise_Popup(self):
        self.create_popup("Asia Cruise", "AsiaCruiseInfo.png")

    def Oceania_Cruise_Popup(self):
        self.create_popup("Oceania Cruise", "OCECruiseInfo.png")

    def create_widgets(self):
        # Upload and load images 
        self.map = tk.PhotoImage(file="Global_Map.png").subsample(1)
        self.red_button = tk.PhotoImage(file="red_button.png").subsample(4)

        # Setup map
        map_label = tk.Label(self.root, image=self.map, bg=self.mapbackground_colour, borderwidth=0)
        map_label.pack(expand=True, fill="both", side="top")

        # Frame for buttons
        button_frame = tk.Frame(self.root, bg=self.mapbackground_colour)
        button_frame.pack(expand=True, fill="both")

        # Buttons for each cruise option
        tk.Button(button_frame, image=self.red_button, text="North America",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.NorthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, text="South America",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.SouthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, text="Europe",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.Europe_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, text="Saudi",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.Saudi_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, text="Asia",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.Asia_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, text="Oceania",
                  bg=self.mapbackground_colour, borderwidth=0,
                  command=self.Oceania_Cruise_Popup).pack(side="left", padx=65,pady=5)

        # Back button
        backbutton_frame = tk.Frame(self.root, bg=self.mapbackground_colour)
        backbutton_frame.pack(expand=True, fill="both")

        tk.Button(backbutton_frame, text="Back", bg="red", fg="white",
                  font=("Times New Roman", 35, "bold"), width=20,
                  command=self.back_to_welcome).pack(side="bottom", ipady=10, padx=10, pady=10)

    def close_and_book(self, popup):
        popup.destroy()
        self.to_customerdetails()

    def back_to_welcome(self):
        self.root.destroy()  # Placeholder

    def to_customerdetails(self):
        print("Booking clicked!")  # Placeholder for customer details page


if __name__ == "__main__":
    MapPage()
