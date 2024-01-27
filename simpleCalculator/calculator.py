import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation_var.get()

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid Input. Please enter a valid choice."

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Python Calculator")

# Create GUI elements
entry_num1 = tk.Entry(window, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

operation_var = tk.StringVar()
operation_var.set('+')  # Default to addition
operation_menu = tk.OptionMenu(window, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(window, width=10)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1, pady=10)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3)

# Start the main event loop
window.mainloop()
