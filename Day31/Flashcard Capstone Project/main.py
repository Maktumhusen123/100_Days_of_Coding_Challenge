from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word ={}
to_learn = {}
try:
    data_frame = pandas.read_csv("words_to_learn.csv")
    # print(data_frame)
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")
# print(to_learn)



def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    french_word = current_word["French"]
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    canvas.itemconfig(canvas_image, image=old_img)
    flip_timer = window.after(3000, change_card)


def change_card():
    canvas.itemconfig(canvas_image, image=new_img)
    canvas.itemconfig(language, fill="white")
    canvas.itemconfig(word, fill="white")
    english_word = current_word["English"]
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=f"{english_word}")


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_card)

canvas = Canvas(width=800, height=526)
old_img = PhotoImage(file="card_front.png")
new_img = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(410, 270, image=old_img)

language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_btn_img = PhotoImage(file="right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=0)

wrong_btn_img = PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)
next_card()
window.mainloop()
