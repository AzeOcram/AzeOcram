import tkinter as tk

#Main Interface

#Title
root = tk.Tk()
root.title("Unit Converter ni Marc")  

#Input value
value_text = tk.Label(root, text="Value:")
value_text.pack(padx=250) 

input_value = tk.Entry(root)
input_value.pack(pady=20)

#From unit
from_text = tk.Label(root, text="From")
from_text.pack() 
from_var = tk.StringVar(value="Select Unit")
options = ["Miles", "Kilometers", "Pounds", "Kilograms", "Inches", "Centimeters"]


from_dropdown = tk.OptionMenu(root, from_var, *options)
from_dropdown.pack(pady=10)

#To unit
to_text = tk.Label(root, text="To")
to_text.pack() 
to_var = tk.StringVar(value="Select Unit")


dropdown = tk.OptionMenu(root, to_var, *options)
dropdown.pack(pady=10)


#Result Text
result_text = tk.Label(root, text="")
result_text.pack(pady=10)


def convert ():
    try:
        value = float(input_value.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        conversion_table = {
            ("Miles", "Kilometers"): 1.60934,
            ("Kilometers", "Miles"): 0.621371,
            ("Pounds", "Kilograms"): 0.453592,
            ("Kilograms", "Pounds"): 2.20462,
            ("Inches", "Centimeters"): 2.54,
            ("Centimeters", "Inches"): 0.393701,
        }

        if (from_unit, to_unit) in conversion_table:
            result = value * conversion_table[(from_unit, to_unit)]
            result_text.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")
        else:
            result_text.config(text="Invalid conversion")

    except ValueError:
        result_text.config(text="Please enter a valid number")


#Convert Button
button = tk.Button(root, text="Convert", command=convert)
button.pack()


root.mainloop()
