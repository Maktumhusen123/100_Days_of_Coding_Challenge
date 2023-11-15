import tkinter

window = tkinter.Tk()
window.title("First GUI Application")
window.minsize(width=300, height=300)

# Label
my_label = tkinter.Label(text="What is your name?", font=("Times New Roman", 14, "bold"))
my_label.pack(side="left")

window.mainloop()
