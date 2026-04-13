from tkinter import *

def display_text():
    output_text = input_text.get()
    my_label["text"] = output_text

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am Label!", font=("Arial", 20, "bold"))
my_label["text"] = "new text"
# my_label.config(text="new text here")

my_label.grid(row=0, column=0)

# Button
submit_btn = Button(text="Click Me!", fg="green", command=display_text)
submit_btn.grid(row=1, column=1)

# Button
submit_btn = Button(text="New Button!", fg="red", command=display_text)
submit_btn.grid(row=0, column=2)

# Entry
input_text = Entry()
input_text.grid(row=2, column=3)

# this will keep the window open and must be the last line of the program
window.mainloop()