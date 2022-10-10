from tkinter import *

window = Tk()
window.config(bg="white")
window.minsize(300,120)

def increase(event=None):
    value = int(Label_1["text"])
    Label_1["text"] = f"{value + 1}"

def decrease(event=None):
    value = int(Label_1["text"])
    Label_1["text"] = f"{value - 1}"


window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

Button_1 = Button(master=window, text="-", fg="red", command=decrease, font="Ariel 20", borderwidth=3, border=4)
Button_1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
window.bind('<Key-->', decrease)

Label_1 = Label(master=window, text="0", fg="black",bg="white", font="Ariel 20")
Label_1.grid(row=0, column=1)

Button_2 = Button(master=window, text="+", fg="green", command=increase, font="Ariel 20", borderwidth=3, border=4)
Button_2.grid(row=0, column=2, sticky="nsew", padx=20, pady=20)
window.bind('<Key-+>', increase)

window.mainloop()
