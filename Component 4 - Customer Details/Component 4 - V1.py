"""""""""""""""""""""""""""
Component 4 - Customer Details v1
"""""""""""""""""""""""""""

import tkinter as tk
from tkinter import messagebox
import json
import os

#file where details will be saved
FILENAME = "Customer_details.json"

def save_response(): #get responses
    response = {
        "full name": name_entry.get(),
        "age": age_entry.get(),
        "location": location_entry.get(),
        "email address": email_entry.get(),
        "cruise": cruise_entry.get(),
        "ticket amount": ticket_entry.get()
        }

    #load already existing file or create a new one
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = [] #if it results in empty file this means it is corrupt
    else: 
        data = []

    #adding new response to file
    data.append(response)

    #save to file
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent =4)
    
    #message to confirm data upload
    messagebox.showinfo("Saved", "Your response has been saved")

    #clear all fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    location_entry(0, tk.END)
    email_entry.delete(0, tk.END)
    cruise_entry.delete(0, tk.END)
    ticket_entry.delete(0, tk.END)


def close_window():
    root.destroy()



#GUI 
root = tk.Tk()
root.title("Booking Form")
root.geometry("500x400")
root.resizable(0,0)

#labels
tk.Label(root, text="Full Name:", ).pack(anchor="w", padx=10, pady=2)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

tk.Label(root, text="Age:", ).pack(anchor="w", padx=10, pady=2)
age_entry = tk.Entry(root, width=40)
age_entry.pack(padx=10)

tk.Label(root, text="Location:", ).pack(anchor="w", padx=10, pady=2)
location_entry = tk.Entry(root, width=40)
location_entry.pack(padx=10)

tk.Label(root, text="Email Address:", ).pack(anchor="w", padx=10, pady=2)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=10)

tk.Label(root, text="Chosen cruise:", ).pack(anchor="w", padx=10, pady=2)
cruise_entry = tk.Entry(root, width=40,)
cruise_entry.pack(padx=10)

tk.Label(root, text="Ticket Amount (max 10 pp):", ).pack(anchor="w", padx=10, pady=2)
ticket_entry = tk.Entry(root, width=40)
ticket_entry.pack(padx=10)

#submit button
submit_button = tk.Button(root, text = "Submit", command = save_response)
submit_button.pack(pady=10)

#close button 
close_button = tk.Button(root, text = "Close", command = close_window)
close_button.pack()


root.mainloop()