import csv
import tkinter as tk
from tkinter import *
from dice import roll_dice
from random import randint
import player
import saver

#from vis import create_vis
count = randint(0,1)

# Show GUI
main = tk.Tk()
main.title("Mensch ärgere dich nicht")
main.geometry("250x250")
saver.create_csv()

def click():
    global count
    result = roll_dice()
    change_label(result)
    saver.write_csv(result)
    if count == 0:
        if result != 6:
            main.title(player.get_player(count))
            count += 1
    elif count == 1: 
        if result != 6:
            main.title(player.get_player(count))
            count -= 1
    print(player.get_player(count), "rolled", )

            

def change_label(result):
    label.config(text = str(result))

button = Button(main, text = "Roll Dice", command = click)
button.pack()

label = Label(main, text = "¯\_(ツ)_/¯")
label.pack()

main.mainloop()


