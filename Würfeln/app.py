import csv
import tkinter as tk
from tkinter import *
from dice import roll_dice
from random import randint
import player
import saver
import os

#from vis import create_vis
count = randint(0,1)
print(count)
counter2 = 1

def click():
    global count
    main.title(player.get_player(count))
    result = roll_dice()
    print(player.get_player(count),"(",count,")", "rolled", result)
    change_label(result)
    saver.write_csv(player.get_player(count), result)
    if count == 0:
        if result != 6:
            main.title(player.get_player(count))
            count = count + 1
    elif count == 1: 
        if result != 6:
            main.title(player.get_player(count))
            count = count - 1

def change_label(result):
    label.config(text = str(result))

def get_out():
    global counter2
    global count
    counter2 = counter2 + 1
    print(count, ": ", counter2)
    result = roll_dice()
    change_label(result)
    if count == 0:
        main.title(player.get_player(count))
        if counter2 % 3 == 0:
            count += 1
    elif count == 1:
        main.title(player.get_player(count))
        if counter2 % 3 == 0:
            count -= 1

def create_viz():
    main.destroy()
    os.system("Rscript Visualization.R")
    print("Created Viz")

# Show GUI
main = tk.Tk()
main.title(player.get_player(count))
main.geometry("250x250")
saver.create_csv()


button = Button(main, text = "Roll Dice", command = click)
button.pack()

label = Label(main, text = "¯\_(ツ)_/¯")
label.pack()

close_button = Button(text = "Quit", command = create_viz)
close_button.pack()

#button2 = Button(main, text = "Ich will raus hier!", command = get_out)
#button2.pack()

main.mainloop()


