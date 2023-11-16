from tkinter import *

window = Tk()
window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input_box = Entry(width=7)
input_box.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="km")
label4.grid(row=1, column=2)


def calculate():
    miles = float(input_box.get())
    km = round(miles * 1.609344)
    # label3["text"] = km
    label3.config(text=f"{km}")


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
window.mainloop()
