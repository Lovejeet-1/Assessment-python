import tkinter as tk
from tkinter import messagebox
import json
import os

# File where details will be saved
FILENAME = "Customer_details.json"

def save_response():
    # Get all entry values
    entries = {
        "Full Name": name_entry,
        "Age": age_entry,
        "Location": location_entry,
        "Email Address": email_entry,
        "Chosen Cruise": cruise_entry,
        "Ticket Amount": ticket_entry
    }

    # Reset all entry highlights
    for entry in entries.values():
        entry.config(highlightthickness=0)

    # Check for blank fields
    for label, entry in entries.items():
        if not entry.get().strip():
            error_label.config(text=f"⚠ {label} cannot be left blank")
            entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            entry.focus()
            return

    # Validate ticket amount
    ticket_value = ticket_entry.get().strip()
    try:
        ticket_num = int(ticket_value)
        if ticket_num < 1 or ticket_num > 10:
            error_label.config(text="⚠ Ticket amount must be between 1 and 10")
            ticket_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            ticket_entry.focus()
            return
    except ValueError:
        error_label.config(text="⚠ Please enter a valid number for ticket amount")
        ticket_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
        ticket_entry.focus()
        return

    # Clear error message if validation passes
    error_label.config(text="")

    # Create response dictionary
    response = {label.lower(): entry.get().strip() for label, entry in entries.items()}

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
    for entry in entries.values():
        entry.delete(0, tk.END)
        entry.config(highlightthickness=0)


def close_window():
    root.destroy()


# GUI setup
root = tk.Tk()
root.title("Booking Form")
root.geometry("500x450")
root.resizable(0, 0)

# Labels + entries
tk.Label(root, text="Full Name:").pack(anchor="w", padx=10, pady=2)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

tk.Label(root, text="Age:").pack(anchor="w", padx=10, pady=2)
age_entry = tk.Entry(root, width=40)
age_entry.pack(padx=10)

tk.Label(root, text="Location:").pack(anchor="w", padx=10, pady=2)
location_entry = tk.Entry(root, width=40)
location_entry.pack(padx=10)

tk.Label(root, text="Email Address:").pack(anchor="w", padx=10, pady=2)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=10)

tk.Label(root, text="Chosen cruise:").pack(anchor="w", padx=10, pady=2)
cruise_entry = tk.Entry(root, width=40)
cruise_entry.pack(padx=10)

tk.Label(root, text="Ticket Amount (1-10):").pack(anchor="w", padx=10, pady=2)
ticket_entry = tk.Entry(root, width=40)
ticket_entry.pack(padx=10)

# Error label (for validation messages)
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=2)

# Frame for buttons (Submit + Close side by side)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Submit", command=save_response)
submit_button.pack(side="left", padx=5)

close_button = tk.Button(button_frame, text="Close", command=close_window)
close_button.pack(side="left", padx=5)

root.mainloop()
