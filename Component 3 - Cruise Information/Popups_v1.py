"""""""""""""""""""""""""""
Component 3 - POPUPS v1
"""""""""""""""""""""""""""
import tkinter as tk

class MapScreen:
    def __init__(self):
        # Window - basic format
        self.root = tk.Tk()
        self.root.title("Map Page")
        self.root.resizable(False, False)
        self.root.geometry("1200x800")
        self.root.configure(bg="white")
        
        open_button = tk.Button(self.root, text="Open New Window", command=self.Europe_Cruise_Popup)
        open_button.pack(pady=50)

        self.root.mainloop()
    
    def Europe_Cruise_Popup(self):  # ✅ Added self
        # Popup window
        popup = tk.Toplevel(self.root)
        popup.title("Europe Cruise")
        popup.resizable(False, False)
        popup.geometry("1000x700")  # ✅ Set popup size (no second root)

        # Import and store image to prevent garbage collection
        self.EU_image = tk.PhotoImage(file="EuropeCruiseInfo.png")
        self.EU_image = self.EU_image.subsample(4)

        # Label for image 
        map_label = tk.Label(popup, bg="black", borderwidth=0, image=self.EU_image)
        map_label.pack(expand=True, fill="both")

        # Frame for booking button
        bookbutton_frame = tk.Frame(popup, bg="red")
        bookbutton_frame.pack(pady=0, padx=0, expand=True, fill="both")

        # Booking button
        button_book = tk.Button(
            bookbutton_frame,
            text="Book".title(),
            bg="red",
            fg="white",
            font=("Times New Roman", 35, "bold"),
            width=20,
            command=self.to_customerdetails
        )
        button_book.pack(side="bottom", ipady=10, padx=10, pady=10)

    def to_customerdetails(self):
        # Placeholder for customer details logic
        print("Navigating to customer details page...")
        self.root.destroy()  # Close main window

if __name__ == "__main__":
    MapScreen()

        