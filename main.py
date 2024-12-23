from tkinter import *

def button_clicked():
    try:
        miles_value = float(input_answer.get())
        result = 1.609 * miles_value
        calculation.config(text=f"{result:.2f}")
    except ValueError:
        calculation.config(text="Invalid input")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

miles = Label(text="Miles", font=("Arial", 15, "bold"))
miles.place(x=275, y=50)

is_equal_to = Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal_to.place(x=50, y=90)

km = Label(text="Km", font=("Arial", 15, "bold"))
km.place(x=290, y=90)

calculation = Label(text="0", font=("Arial", 15, "bold"))
calculation.place(x=210, y=90)

input_answer = Entry(width=10, font=("Arial", 12, "bold"))
input_answer.place(x=170, y=55)

button = Button(text="Calculate", command=button_clicked)
button.place(x=170, y=130)


window.mainloop()