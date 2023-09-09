from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# word_list = {}


# -------------------------Function button-----------------------#
try:
    i = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    ni = pandas.read_csv("french_words.csv")
    n = ni.to_dict(orient='records')
else:
    n = i.to_dict(orient='records')

def rt():
    global word_list, timer
    window.after_cancel(timer)
    word_list = random.choice(n)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=word_list["French"], fill="black")
    canvas.itemconfig(card_bg, image=image)
    timer = window.after(3000, func=card)

def rem():
    n.remove(word_list)

    data = pandas.DataFrame(n)
    data.to_csv("words_to_learn.csv", index=False)
    rt()
# -------------------------Card Flip---------------------- #

def card():

    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=word_list["English"], fill="white")
    canvas.itemconfig(card_bg, image=flip_image)
# -------------------------UI----------------------------- #

window = Tk()
window.title("Languages Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_image = PhotoImage(file="card_back.png")
image = PhotoImage(file="card_front.png")
card_bg = canvas.create_image(400, 263, image=image)
title = canvas.create_text(400, 158, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 280, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

rt()

window.after_cancel(card)
wrong_image = PhotoImage(file="wrong.png")
button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=rt)
button.grid(column=0, row=1)

right_image = PhotoImage(file="right.png")
button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=rem)
button.grid(column=1, row=1)


window.mainloop()
