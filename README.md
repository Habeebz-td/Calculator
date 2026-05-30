# Calculator App 🧮

A simple GUI calculator built with Python and Tkinter. Supports addition, subtraction, multiplication, and division — and you can use either the on-screen buttons or your actual keyboard to type.

This was my first project with a visual interface. Up until this point everything I built ran in the terminal, so getting something to actually appear on screen felt like a big deal.

---

## What it does

- Clean button layout (0–9, operators, decimal, clear, equals)
- Works with **mouse clicks** or **keyboard input**
- Handles division by zero gracefully instead of crashing
- Displays errors for invalid input

---

## How to run it

Make sure Python is installed (Python 3 recommended). Tkinter comes built-in so no extra installs needed.

```bash
python calculator.py
```

A window will pop up — that's it.

---

## Keyboard shortcuts

| Key | Action |
|---|---|
| `0–9`, `.` | Enter numbers |
| `+`, `-`, `*`, `/` | Operators |
| `Enter` | Calculate (same as `=`) |
| `Backspace` | Clear the display |

---

## How it works

The display is a Tkinter `Entry` widget. When you press `=`, the `calculate()` function reads whatever's in the entry box, splits it on the operator, converts both parts to floats, and calls the right function (`addition`, `subtraction`, etc.).

Each operation is its own function:

```python
def addition(a, b):      return a + b
def subtraction(a, b):   return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
```

---

## Things I learnt building this

- How Tkinter's grid layout system works
- Binding keyboard events with `root.bind("<Key>", ...)`
- Using lambda functions to pass arguments to button commands
- Input parsing and basic error handling with try/except

---

## Known limitations

- Only handles one operator per calculation (no chained expressions like `5+3*2`)
- No bracket support
- Negative numbers need a workaround

These are the natural next steps if I were to keep building on it.

---

## Built with

- Language: Python 3
- Library: Tkinter (built-in)
- Interface: GUI window
