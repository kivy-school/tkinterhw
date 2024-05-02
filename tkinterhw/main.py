import tkinter as tk

# Create the main window
root = tk.Tk()
# Set window title
root.title("Welcome to Kivy School!")
# Set min window size
root.minsize(450, 100)
# Set window to always be on top (remove this line for a regular GUI)
root.attributes('-topmost',True)

# Create label
label = tk.Label(root, text="Hello, World!")

# Lay out label
label.pack()

# Run forever!
root.mainloop()