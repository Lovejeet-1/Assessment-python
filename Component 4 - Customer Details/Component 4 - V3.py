import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "Customer_details.json"

class BookingForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking Form")
        self.root.geometry("500x450")
        self.root.resizable(0, 0)

        self.entries = {}  # Dictionary to store entry widgets

        # Create form fields
        self.create_field("Full Name")
        self.create_field("Age")
        self.create_field("Location")
        self.create_field("Email Address")
        self.create_field("Chosen Cruise")
        self.create_field("Ticket Amount (1-10)")

        # Error label
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack(pady=2)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        submit_button = tk.Button(button_frame, text="Submit", command=self.save_response)
        submit_button.pack(side="left", padx=5)

        close_button = tk.Button(button_frame, text="Close", command=self.close_window)
        close_button.pack(side="left", padx=5)

    def create_field(self, label_text):
        tk.Label(self.root, text=f"{label_text}:").pack(anchor="w", padx=10, pady=2)
        entry = tk.Entry(self.root, width=40)
        entry.pack(padx=10)
        self.entries[label_text] = entry

    def save_response(self):
        # Reset highlights
        for entry in self.entries.values():
            entry.config(highlightthickness=0)

        # Check for blank fields
        for label, entry in self.entries.items():
            if not entry.get().strip():
                self.error_label.config(text=f"⚠ {label} cannot be left blank")
                entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
                entry.focus()
                return

        # Validate ticket amount
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

        # Clear error message if validation passes
        self.error_label.config(text="")

        # Collect response
        response = {label.lower(): entry.get().strip() for label, entry in self.entries.items()}

        # Load existing data or create a new list
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(response)

        # Save to file
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Saved", "Your response has been saved")

        # Clear all fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)
            entry.config(highlightthickness=0)

    def close_window(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BookingForm(root)
    root.mainloop()
