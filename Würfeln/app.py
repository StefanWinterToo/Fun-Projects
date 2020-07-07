import tkinter as tk
from tkinter import *
from dice import roll_dice

# Show GUI
main = tk.Tk()
main.title("Dice")
main.geometry("250x250")

def click():
    result = roll_dice()
    print(result)
    change_label()

def change_label():
    label.config(text = str(roll_dice()))

button = Button(main, text = "Roll Dice", command = click)
button.pack()

label = Label(main, text = "Hallo")
label.pack()

main.mainloop()