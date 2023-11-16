from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=300, height=300)
window.title("Pomodoro")
window.config(padx=10, pady=30, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Adding Image using Canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # provide same width and height as per image
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start")
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.grid(row=2, column=2)

checkmark_label = Label(text="✔", fg=GREEN)
checkmark_label.grid(row=3, column=1)
window.mainloop()
