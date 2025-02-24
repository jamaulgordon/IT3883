# Program Name: Assignment3.py
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: Lab2
# Due Date: 02/23/25
# Purpose: This program creates a GUI-based conversion tool that converts Miles per Gallon (MPG) to Kilometers per Liter (KM/L). The result updates dynamically as the user types.
# Resources Used: Tkinter documentation, Python official docs

import tkinter as tk

# Conversion factor
CONVERSION_FACTOR = 0.425143707  

class MPGConverterApp:
    """A GUI application to convert Miles per Gallon (MPG) to Kilometers per Liter (KM/L)."""

    def __init__(self, root):
        self.root = root
        self.root.title("MPG to KM/L Converter")
        self.root.geometry("350x200")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        """Creates and arranges all GUI components."""
        tk.Label(self.root, text="Miles per Gallon (MPG):", font=("Arial", 10)).pack(pady=5)

        self.entry_mpg = tk.Entry(self.root, font=("Arial", 12))
        self.entry_mpg.pack()
        self.entry_mpg.bind("<KeyRelease>", self.convert_mpg_to_kml)  # Dynamic update

        self.result_label = tk.Label(self.root, text="KM/L: 0.000", font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=10)

    def convert_mpg_to_kml(self, event=None):
        """Converts MPG to KM/L and updates the result dynamically."""
        try:
            mpg = float(self.entry_mpg.get())
            kml = mpg * CONVERSION_FACTOR
            self.result_label.config(text=f"KM/L: {kml:.3f}")
        except ValueError:
            self.result_label.config(text="Invalid Input", fg="red")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MPGConverterApp(root)
    root.mainloop()
