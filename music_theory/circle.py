import tkinter as tk
from tkinter import Menu
import math

# Function to draw the circle of fifths
def draw_circle_of_fifths(canvas):
    canvas.delete("all")  # Clear the canvas
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    radius = min(width, height) // 3  # Set the radius
    center_x, center_y = width // 2, height // 2  # Find the center

    # List of sharp keys in the circle of fifths
    sharp_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]
    # List of flat keys in the circle of fifths
    flat_keys = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb", "Bbb", "Ebb", "Abb"]

    # Draw the sharp keys
    for i, key in enumerate(sharp_keys):
        angle = math.radians(-i * 30)  # 30 degrees apart
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        canvas.create_text(x, y, text=key, font=("Arial", 12), fill="blue")

    # Draw the flat keys
    for i, key in enumerate(flat_keys):
        angle = math.radians(-i * 30 + 180)  # 30 degrees apart, starting from the opposite side
        x = center_x + radius * math.cos(angle) + 50
        y = center_y + radius * math.sin(angle)
        canvas.create_text(x, y, text=key, font=("Arial", 12), fill="red")

# Create the main window
root = tk.Tk()
root.title("Circle of Fifths")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Circle of Fifths", command=lambda: draw_circle_of_fifths(canvas))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()
