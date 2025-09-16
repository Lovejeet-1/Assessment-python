import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "Customer_details.json"

# Colors
welcomebuttons_colour = "#2cdfdd"
welcomebackground_colour = "#f3f1eb"
mapbackground_colour = "#d4c29a"


class WelcomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome")
        self.root.resizable(False, False)
        self.root.geometry("1200x800")
        self.root.configure(bg=welcomebackground_colour)
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.logo = tk.PhotoImage(file="Logofinal.png").subsample(2)
        logo_label = tk.Label(self.root, image=self.logo, bg=welcomebackground_colour)
        logo_label.pack(side="top", ipady=40, padx=10, pady=40, expand=True, fill="both")

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
        MapPage()

#Component 2 and 3
class MapPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Map Page")
        self.root.resizable(False, False)
        self.root.geometry("1600x1000")
        self.root.configure(bg="white")
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
        map_label = tk.Label(popup, bg=mapbackground_colour, image=self.current_image)
        map_label.pack(expand=True, fill="both")

        button_frame = tk.Frame(popup, bg=mapbackground_colour)
        button_frame.pack(expand=True, fill="both", pady=10)

        tk.Button(
            button_frame,
            text="Book",
            bg="red",
            fg="white",
            font=("Times New Roman", 25, "bold"),
            width=15,
            command=lambda: self.open_booking(popup)
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

        map_label = tk.Label(self.root, image=self.map, bg=mapbackground_colour, borderwidth=0)
        map_label.pack(expand=True, fill="both", side="top")

        button_frame = tk.Frame(self.root, bg=mapbackground_colour)
        button_frame.pack(expand=True, fill="both")

        tk.Button(button_frame, image=self.red_button, compound="center", text="North America",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.NorthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="South America",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.SouthAmerica_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Europe",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.Europe_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Saudi",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.Saudi_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Asia",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.Asia_Cruise_Popup).pack(side="left", padx=65, pady=5)

        tk.Button(button_frame, image=self.red_button, compound="center", text="Oceania",
                  bg=mapbackground_colour, borderwidth=0, fg="white",
                  command=self.Oceania_Cruise_Popup).pack(side="left", padx=65, pady=5)

        backbutton_frame = tk.Frame(self.root, bg=mapbackground_colour)
        backbutton_frame.pack(expand=True, fill="both")

        tk.Button(backbutton_frame, text="Back", bg="red", fg="white",
                  font=("Times New Roman", 35, "bold"), width=20,
                  command=self.back_to_welcome).pack(side="bottom", ipady=10, padx=10, pady=10)

    def open_booking(self, popup):
        popup.destroy()
        self.root.destroy()
        BookingForm()

    def back_to_welcome(self):
        self.root.destroy()
        WelcomePage()


class BookingForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Booking Form")
        self.root.geometry("500x450")
        self.root.resizable(0, 0)

        self.entries = {}
        self.create_field("Full Name")
        self.create_field("Age")
        self.create_field("Location")
        self.create_field("Email Address")
        self.create_field("Chosen Cruise")
        self.create_field("Ticket Amount (1-10)")

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack(pady=2)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Submit", command=self.save_response).pack(side="left", padx=5)
        tk.Button(button_frame, text="Close", command=self.close_and_back).pack(side="left", padx=5)

        self.root.mainloop()

    def create_field(self, label_text):
        tk.Label(self.root, text=f"{label_text}:").pack(anchor="w", padx=10, pady=2)
        entry = tk.Entry(self.root, width=40)
        entry.pack(padx=10)
        self.entries[label_text] = entry

    def save_response(self):
        for entry in self.entries.values():
            entry.config(highlightthickness=0)

        for label, entry in self.entries.items():
            if not entry.get().strip():
                self.error_label.config(text=f"⚠ {label} cannot be left blank")
                entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
                entry.focus()
                return

        ticket_entry = self.entries["Ticket Amount (1-10)"]
        ticket_value = ticket_entry.get().strip()
        try:
            ticket_num = int(ticket_value)
            if ticket_num < 1 or ticket_num > 10:
                self.error_label.config(text="⚠ Ticket amount must be between 1 and 10")
                ticket_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
                ticket_entry.focus()
                return
        except ValueError:
            self.error_label.config(text="⚠ Please enter a valid number for ticket amount")
            ticket_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            ticket_entry.focus()
            return

        self.error_label.config(text="")
        response = {label.lower(): entry.get().strip() for label, entry in self.entries.items()}

        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(response)
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Saved", "Your response has been saved")
        for entry in self.entries.values():
            entry.delete(0, tk.END)
            entry.config(highlightthickness=0)

    def close_and_back(self):
        self.root.destroy()
        MapPage()


if __name__ == "__main__":
    WelcomePage()
