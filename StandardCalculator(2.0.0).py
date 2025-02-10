from tkinter import *
import tkinter.font as tkFont
import math

calc = Tk()
golden_ratio = 1.618
window_width = 320
window_height = int(window_width * golden_ratio)
calc.geometry(f"{window_width}x{window_height}+700+300")
calc.minsize(window_width, window_height)
calc.title('Calculator')

calc.configure(bg="Grey")

op = ""

def btn(x):
    global op
    op = op + x
    if op.find('0') == 0:
        op = op[1:]
    textinput.set(op)

def eq():
    global op
    try:
        result = str(eval(op))
        textinput.set(result)
        op = result
    except:
        textinput.set("Error")
        op = ""

def c():
    global op
    op = ""
    textinput.set("")

def backspace():
    global op
    op = op[:-1]
    textinput.set(op)

def reciprocal():
    global op
    try:
        result = str(1 / eval(op))
        textinput.set(result)
        op = result
    except:
        textinput.set("Error")
        op = ""

def square():
    global op
    try:
        result = str(eval(op) ** 2)
        textinput.set(result)
        op = result
    except:
        textinput.set("Error")
        op = ""

def square_root():
    global op
    try:
        result = str(math.sqrt(eval(op)))
        textinput.set(result)
        op = result
    except:
        textinput.set("Error")
        op = ""

def percentage():
    global op
    try:
        result = str(eval(op) / 100)
        textinput.set(result)
        op = result
    except:
        textinput.set("Error")
        op = ""

def clear_entry():
    global op
    op = "0"
    textinput.set(op)

prev_width = window_width
prev_height = window_height
resize_timer = None

def resize_fonts(event):
    global prev_width, prev_height, resize_timer
    if resize_timer is not None:
        calc.after_cancel(resize_timer)
    resize_timer = calc.after(500, apply_resize)

def apply_resize():
    global prev_width, prev_height
    current_width = calc.winfo_width()
    current_height = calc.winfo_height()
    if abs(current_width - prev_width) > 10 or abs(current_height - prev_height) > 10:
        prev_width = current_width
        prev_height = current_height
        entry_font_size = min(28, max(12, int(entry_font.cget("size")) + 2))
        button_font_size = min(14, max(10, int(button_font.cget("size")) + 2))
        entry_font.configure(size=entry_font_size)
        button_font.configure(size=button_font_size)
        button_bold_font.configure(size=button_font_size)

textinput = StringVar(value="0")
entry_font = tkFont.Font(family='Segoe UI', size=28)
e1 = Entry(calc, font=entry_font, bd=4, textvariable=textinput, justify="right", bg="lightgray")
e1.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=10)

button_font = tkFont.Font(family='Segoe UI', size=12)
button_bold_font = tkFont.Font(family='Segoe UI', size=12, weight='bold')
button_height = window_height // 10
button_width = window_width // 4

calc.grid_rowconfigure(0, weight=1)
calc.grid_columnconfigure(0, weight=1)
calc.grid_columnconfigure(1, weight=1)
calc.grid_columnconfigure(2, weight=1)
calc.grid_columnconfigure(3, weight=1)

def on_enter(e):
    e.widget['background'] = 'slategray'

def on_leave(e):
    e.widget['background'] = 'lightgray'

def create_button(text, row, column, command, bg='lightgray', fg='black'):
    btn = Button(calc, text=text, font=button_font, bd=4, command=command, bg=bg, fg=fg)
    btn.grid(row=row, column=column, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

create_button("+/-", 7, 0, lambda: btn('+/-'))
create_button("0", 7, 1, lambda: btn('0'))
create_button(".", 7, 2, lambda: btn('.'))
create_button("=", 7, 3, eq)

create_button("1", 6, 0, lambda: btn('1'))
create_button("2", 6, 1, lambda: btn('2'))
create_button("3", 6, 2, lambda: btn('3'))
create_button("+", 6, 3, lambda: btn('+'))

create_button("4", 5, 0, lambda: btn('4'))
create_button("5", 5, 1, lambda: btn('5'))
create_button("6", 5, 2, lambda: btn('6'))
create_button("-", 5, 3, lambda: btn('-'))

create_button("7", 4, 0, lambda: btn('7'))
create_button("8", 4, 1, lambda: btn('8'))
create_button("9", 4, 2, lambda: btn('9'))
create_button("*", 4, 3, lambda: btn('*'))

create_button("¹/ₓ", 3, 0, reciprocal)
create_button("x²", 3, 1, square)
create_button("√x", 3, 2, square_root)
create_button("÷", 3, 3, lambda: btn('/'))

create_button("%", 2, 0, percentage)
create_button("CE", 2, 1, clear_entry)
create_button("C", 2, 2, c)
create_button("←", 2, 3, backspace)

for i in range(8):
    calc.grid_rowconfigure(i, weight=1)
for j in range(4):
    calc.grid_columnconfigure(j, weight=1)

calc.bind("<Configure>", resize_fonts)
calc.mainloop()
