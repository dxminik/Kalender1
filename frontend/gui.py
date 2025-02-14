
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/dominikbechthold/Library/Mobile Documents/com~apple~CloudDocs/A - Studium/Python/1/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("640x420")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 420,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    18.000000000000014,
    49.0,
    549.0,
    311.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    9.000000000000014,
    59.0,
    anchor="nw",
    text="Dein tägliches Tagebuh",
    fill="#000000",
    font=("RobotoRoman Medium", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="groove"
)
button_1.place(
    x=18.000000000000014,
    y=8.000000000000004,
    width=47.0,
    height=34.0
)

canvas.create_rectangle(
    379.0,
    8.000000000000004,
    549.0,
    42.0,
    fill="#D9D9D9",
    outline=""
    )

canvas.create_text(
    430.0,
    18.000000000000004,
    anchor="nw",
    text="Search...",
    fill="#000000",
    font=("RobotoRoman Medium", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
