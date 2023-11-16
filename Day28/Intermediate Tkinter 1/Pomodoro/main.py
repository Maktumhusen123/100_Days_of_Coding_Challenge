from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmark_label.config(text=marks)


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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmark_label = Label(fg=GREEN)
checkmark_label.grid(row=3, column=1)
window.mainloop()
