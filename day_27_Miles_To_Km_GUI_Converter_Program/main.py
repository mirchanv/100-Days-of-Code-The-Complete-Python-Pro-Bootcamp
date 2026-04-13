from tkinter import *

def convert_mile_to_km():
    clear_km_field()
    miles_to_convert = float(miles.get())
    result = miles_to_convert * 1.609
    km.insert(END, '{0:.2f}'.format(result))
    display_output_text()

def clear_km_field():
    km.delete(0, END)

def display_output_text():
    output.config(text=f"{miles.get()} miles is equal to {km.get()} kms")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = Entry(justify="center")
miles.grid(row=0, column=0)

equals_label = Label(text=" = ", font=("Arial", 20, "bold"))
equals_label.grid(row=0, column=1)

km = Entry(justify="center")
km.grid(row=0, column=2)

miles_label = Label(text="Mile")
miles_label.grid(row=1, column=0)

km_label = Label(text="Kilometre")
km_label.grid(row=1, column=2)

convert_btn = Button(text="Convert", command=convert_mile_to_km)
convert_btn.grid(row=2, column=0, columnspan=3)

output = Label()
output.grid(row=3, column=0, columnspan=3)
output.config(pady=15)

# this will keep the window open and must be the last line of the program
window.mainloop()