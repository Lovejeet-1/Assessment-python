import tkinter as tk

welcomebuttons_colour = "#2cdfdd"
welcomebackground_colour = "#f3f1eb"

class WelcomePage:
    def __init__(self):
        self.root = tk.Tk()
        # Window
        self.root.title("Welcome")
        self.root.resizable(False, False)
        self.root.geometry("1200x800")
        self.root.configure(bg=welcomebackground_colour)

        self.create_widgets_welcome()
        self.root.mainloop()

    def create_widgets_welcome(self):
        # Load logo
        self.logo = tk.PhotoImage(file="Logofinal.png").subsample(2)

        logo_label = tk.Label(self.root, image=self.logo, bg=welcomebackground_colour)
        logo_label.pack(side="top", ipady=40, padx=10, pady=40, expand=True, fill="both")

        # Continue button (opens MapPage)
        button_continue = tk.Button(
            self.root,
            text="Continue",
            bg=welcomebuttons_colour,
            fg="white",
            font=("Times New Roman", 35, "bold"),
            width=20,
            command=self.to_map
        )
        button_continue.pack(side="right", ipady=10, padx=10, pady=10)

        # Quit button (closes program)
        button_quit = tk.Button(
            self.root,
            text="Quit",
            bg=welcomebuttons_colour,
            fg="white",
            font=("Times New Roman", 35, "bold"),
            width=20,
            command=self.quit
        )
        button_quit.pack(side="top", ipady=10, padx=10, pady=10)

    def quit(self):
        self.root.destroy()

    def to_map(self):
        self.root.destroy()
        MapPage() #Launch Component 2


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

    def create_popup(self, title, image_path):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.resizable(False, False)
        popup.geometry("600x500")

        popup.transient(self.root)
        popup.grab_set()

        self.current_image = tk.PhotoImage(file=image_path).subsample(3)

        map_label = tk.Label(popup, bg=self.mapbackground_colour, image=self.current_image)
        map_label.pack(expand=True, fill="both")

        button_frame = tk.Frame(popup, bg=self.mapbackground_colour)
        button_frame.pack(expand=True, fill="both", pady=10)

        tk.Button(
            button_frame,
            text="Book",
            bg="red",
            fg="white",
            font=("Times New Roman", 25, "bold"),
            width=15,
            command=lambda: self.close_and_book(popup)
        ).pack(side="left", expand=True, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Close",
            bg="red",
            fg="white",
            font=("Times New Roman", 25, "bold"),
            width=15,
            command=popup.destroy
        ).pack(side="right", expand=True, padx=10, pady=10)

        popup.wait_window(popup)

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
        self.map = tk.PhotoImage(file="Global_Map.png").subsample(1)
        self.red_button = tk.PhotoImage(file="red_button.png").subsample(4)

        map_label = tk.Label(self.root, image=self.map, bg=self.mapbackground_colour, borderwidth=0)
        map_label.pack(expand=True, fill="both", side="top")

        button_frame = tk.Frame(self.root, bg=self.mapbackground_colour)
        button_frame.pack(expand=True, fill="both")

        tk.Button(button_frame, image=self.red_button, compound="center", text="North America",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white",
                  command=self.NorthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="South America",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white",
                  command=self.SouthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Europe",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white", 
                  command=self.Europe_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Saudi",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white", 
                  command=self.Saudi_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Asia",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white", 
                  command=self.Asia_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Oceania",
                  bg=self.mapbackground_colour, borderwidth=0,  fg="white", 
                  command=self.Oceania_Cruise_Popup).pack(side="left", padx=65, pady=5)

        backbutton_frame = tk.Frame(self.root, bg=self.mapbackground_colour)
        backbutton_frame.pack(expand=True, fill="both")

        tk.Button(backbutton_frame, text="Back", bg="red", fg="white",
                  font=("Times New Roman", 35, "bold"), width=20,
                  command=self.back_to_welcome).pack(side="bottom", ipady=10, padx=10, pady=10)

    def close_and_book(self, popup):
        popup.destroy()
        self.to_customerdetails()

    def back_to_welcome(self):
        self.root.destroy()
        WelcomePage()  # Relaunch Component 1

    def to_customerdetails(self):
        print("Booking clicked!")  # Placeholder


if __name__ == "__main__": 
        WelcomePage()