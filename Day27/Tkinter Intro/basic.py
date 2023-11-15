from tkinter import *

window = Tk()
window.title("First GUI Application")
window.minsize(width=1000, height=300)

# Label
my_label = Label(text="What is your name?", font=("Times New Roman", 14, "bold"))
my_label.pack()


def button_clicked():
    my_label["text"] = textbox.get()


# Button
my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry
textbox = Entry(width=40)
textbox.insert(END, "Enter your name")
textbox.focus()
textbox.pack()

# Textarea
textarea = Text(height=5, width=30)
textarea.insert(END, "Type something")
textarea.pack()


# Checkbox
def checkbox_clicked():
    print(checked_state.get())


checked_state = IntVar()
checkbox = Checkbutton(text="Coding", variable=checked_state, command=checkbox_clicked)
checkbox.pack()


# Radio button
def radio_checked():
    print(radio_state.get())


radio_state = IntVar()
radio1 = Radiobutton(text="Reading", variable=radio_state, value=1, command=radio_checked)
radio2 = Radiobutton(text="Writing", variable=radio_state, value=2, command=radio_checked)
radio1.pack()
radio2.pack()


# Spinbox
def spinbox_val():
    print(spin_box.get())


spin_box = Spinbox(from_=1, to=10, command=spinbox_val)
spin_box.pack()


# Scale
def scale_val(value):
    print(value)


scale = Scale(from_=1, to=30, command=scale_val)
scale.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# List box
listbox = Listbox(height=6)
fruits = ["apple", "banana", "papaya"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
