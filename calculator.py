import tkinter as tk
def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

def update_display(num):
    display.insert(tk.END, num)

def calculate():
    try:    
        equation = display.get()
        result = "Error"

        if "+" in equation:
            parts = equation.split("+")

            num1 = float(parts[0])
            num2 = float(parts[1])

            result = addition(num1, num2)

        elif "-" in equation:
            parts = equation.split("-")

            num1 = float(parts[0])
            num2 = float(parts[1])

            result = subtraction(num1, num2)

        elif "*" in equation:
            parts = equation.split("*")

            num1 = float(parts[0])
            num2 = float(parts[1])

            result = multiplication(num1, num2)

        elif "/" in equation:
            parts = equation.split("/")

            num1 = float(parts[0])
            num2 = float(parts[1])

            result = division(num1, num2)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except (ValueError, IndexError, ZeroDivisionError):
        display.delete(0, tk.END)
        display.insert(0, "Error: Invalid input.")


def clear_display():
    display.delete(0, tk.END)


def key_pressed(event):
    key = event.char
    # Check if the key is a number or operator
    if key in "0123456789.+-*/":
        update_display(key)
    # Check if the user pressed Enter (for equals)
    elif key == "\r":  # "\r" is the Enter key
        calculate()
    # Check if the user pressed Backspace (for clear)
    elif key == "\x08": # "\x08" is the Backspace key
        clear_display()



root = tk.Tk()
root.config(bg="gray")
root.title("Simple Calculator")

# Buttons
bt1 = tk.Button(root, text="7", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("7"))
bt1.grid(row=2, column=0)
bt2 = tk.Button(root, text="8", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("8"))
bt2.grid(row=2, column=1)
bt3 = tk.Button(root, text="9", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("9"))
bt3.grid(row=2, column=2)
bt4 = tk.Button(root, text="4", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("4"))
bt4.grid(row=3, column=0)
bt5 = tk.Button(root, text="5", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("5"))
bt5.grid(row=3, column=1)
bt6 = tk.Button(root, text="6", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("6"))
bt6.grid(row=3, column=2)
bt7 = tk.Button(root, text="1", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("1"))
bt7.grid(row=4, column=0)
bt8 = tk.Button(root, text="2", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("2"))
bt8.grid(row=4, column=1)
bt9 = tk.Button(root, text="3", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("3"))
bt9.grid(row=4, column=2)
bt11 = tk.Button(root, text="0", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("0"))
bt11.grid(row=5, column=1)
bt12 = tk.Button(root, text=".", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("."))
bt12.grid(row=5, column=2)
bt13 = tk.Button(root, text="=", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: calculate())
bt13.grid(row=5, column=3)
bt14 = tk.Button(root, text="-", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("-"))
bt14.grid(row=2, column=3)
bt15 = tk.Button(root, text="+", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("+"))
bt15.grid(row=3, column=3)
bt16 = tk.Button(root, text="/", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("/"))
bt16.grid(row=1, column=2)
bt17 = tk.Button(root, text="*", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: update_display("*"))
bt17.grid(row=1, column=1)
bt18 = tk.Button(root, text="C", bg="grey", activebackground="cyan", height=2, width=10, borderwidth=5, command=lambda: clear_display())
bt18.grid(row=1, column=0)

display = tk.Entry(root, bg="black", fg="green", font="bold", width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Bind the root window to all key presses
root.bind("<Key>", key_pressed)

root.mainloop()