import csv
import tkinter as tk
from tkinter import *
from dice import roll_dice
import saver

# Show GUI
main = tk.Tk()
main.title("Dice")
main.geometry("250x250")
saver.create_csv()

def click():
    result = roll_dice()
    print(result)
    change_label(result)
    saver.write_csv(result)

def change_label(result):
    label.config(text = str(result))

button = Button(main, text = "Roll Dice", command = click)
button.pack()

label = Label(main, text = "¯\_(ツ)_/¯")
label.pack()

main.mainloop()