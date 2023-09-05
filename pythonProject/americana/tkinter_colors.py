import tkinter as tk
import random


def change_background_color():
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    root.configure(bg=color)
    color_button.configure(bg=color)


root = tk.Tk()
root.title("Background Color Example")

color_button = tk.Button(root, text="Change Background Color", command=change_background_color)
color_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()
