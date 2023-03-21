
from tkinter import *

BLACK = "#000"
YELLOW = "#f7f5dd"
BLUE = "#023047"
FONT_NAME = "Montserrat"

window = Tk()
window.title("Service Learning")
window.config(padx=100, pady=50, bg=YELLOW)

heading_label = Label(text="Service Learning", font=(
    FONT_NAME, 50), fg=BLACK, bg=YELLOW)
heading_label.grid(column=1, row=0)

start_button = Button(text="Enable Gesture Communication", font=(50),
                         highlightthickness=2,  width=50, height=2)
start_button.grid(column=1, row=2)

canvas = Canvas(width=500, height=400, bg=YELLOW, highlightthickness=0)
train_img = PhotoImage(file="train_.png")
canvas.create_image(200, 200, image=train_img)

canvas.grid(column=1, row=1)


window.mainloop()
