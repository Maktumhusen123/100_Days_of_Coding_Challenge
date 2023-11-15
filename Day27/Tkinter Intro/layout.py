# There are 3 layout managers: pack(), place(x=, y=) and grid(column=, row=)
from tkinter import *

window = Tk()
window.title("First GUI Application")
window.minsize(width=1000, height=300)
window.config(padx=20, pady=10)     # padx and pady can be used for padding

# Label
my_label = Label(text="What is your name?", font=("Times New Roman", 14, "bold"))
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


def button_clicked():
    my_label["text"] = textbox.get()


my_button1 = Button(text="Click Me", command=button_clicked)
my_button1.grid(column=2, row=0)

# Button
my_button2 = Button(text="Click Me", command=button_clicked)
my_button2.grid(column=1, row=1)

# Entry
textbox = Entry(width=40)
textbox.insert(END, "Enter your name")
textbox.focus()
textbox.grid(column=3, row=2)

window.mainloop()
