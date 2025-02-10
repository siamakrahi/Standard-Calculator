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
e1 = Entry(calc, font=entry_font, bd=4, 
            textvariable=textinput, justify="right")
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


btnGrade = Button(calc, text="+/-", font=button_font, bd=4, command=lambda: btn('+/-'), bg='lightgray', fg='black')
btnGrade.grid(row=7, column=0, sticky="nsew")

btn0 = Button(calc, text="0", font=button_font, bd=4, command=lambda: btn('0'), bg='lightgray', fg='black')
btn0.grid(row=7, column=1, sticky="nsew")

btnDOT = Button(calc, text=".", font=button_font, bd=4, command=lambda: btn('.'), bg='lightgray', fg='black')
btnDOT.grid(row=7, column=2, sticky="nsew")

btnEqual = Button(calc, text="=", font=button_bold_font, bd=4, command=eq, bg='lightgray', fg='black')
btnEqual.grid(row=7, column=3, sticky="nsew")

btn1 = Button(calc, text="1", font=button_font, bd=4, command=lambda: btn('1'), bg='lightgray', fg='black')
btn1.grid(row=6, column=0, sticky="nsew")

btn2 = Button(calc, text="2", font=button_font, bd=4, command=lambda: btn('2'), bg='lightgray', fg='black')
btn2.grid(row=6, column=1, sticky="nsew")

btn3 = Button(calc, text="3", font=button_font, bd=4, command=lambda: btn('3'), bg='lightgray', fg='black')
btn3.grid(row=6, column=2, sticky="nsew")

btnAdd = Button(calc, text="+", font=button_font, bd=4, command=lambda: btn('+'), bg='lightgray', fg='black')
btnAdd.grid(row=6, column=3, sticky="nsew")

btn4 = Button(calc, text="4", font=button_font, bd=4, command=lambda: btn('4'), bg='lightgray', fg='black')
btn4.grid(row=5, column=0, sticky="nsew")

btn5 = Button(calc, text="5", font=button_font, bd=4, command=lambda: btn('5'),bg='lightgray', fg='black')
btn5.grid(row=5, column=1, sticky="nsew")

btn6 = Button(calc, text="6", font=button_font, bd=4, command=lambda: btn('6'), bg='lightgray', fg='black')
btn6.grid(row=5, column=2, sticky="nsew")

btnSub = Button(calc, text="-", font=button_bold_font, bd=4, command=lambda: btn('-'), bg='lightgray', fg='black')
btnSub.grid(row=5, column=3, sticky="nsew")

btn7 = Button(calc, text="7", font=button_font, bd=4, command=lambda: btn('7'), bg='lightgray', fg='black')
btn7.grid(row=4, column=0, sticky="nsew")

btn8 = Button(calc, text="8", font=button_font, bd=4, command=lambda: btn('8'), bg='lightgray', fg='black')
btn8.grid(row=4, column=1, sticky="nsew")

btn9 = Button(calc, text="9", font=button_font, bd=4, command=lambda: btn('9'), bg='lightgray', fg='black')
btn9.grid(row=4, column=2, sticky="nsew")

btnMul = Button(calc, text="*", font=button_bold_font, bd=4, command=lambda: btn('*'), bg='lightgray', fg='black')
btnMul.grid(row=4, column=3, sticky="nsew")

btn1x = Button(calc, text="¹/ₓ", font=button_bold_font, bd=4, command=reciprocal, bg='lightgray', fg='black')
btn1x.grid(row=3, column=0, sticky="nsew")

btn2x = Button(calc, text="x²", font=button_bold_font, bd=4, command=square, bg='lightgray', fg='black')
btn2x.grid(row=3, column=1, sticky="nsew")

btnx2 = Button(calc, text="√x", font=button_bold_font, bd=4, command=square_root, bg='lightgray', fg='black')
btnx2.grid(row=3, column=2, sticky="nsew")

btnDiv = Button(calc, text="÷", font=button_bold_font, bd=4, command=lambda: btn('/'), bg='lightgray', fg='black')
btnDiv.grid(row=3, column=3, sticky="nsew")

btnP = Button(calc, text="%", font=button_bold_font, bd=4, command=percentage, bg='lightgray', fg='black')
btnP.grid(row=2, column=0, sticky="nsew")

btnCE = Button(calc, text="CE", font=button_bold_font, bd=4, command=clear_entry, bg='lightgray', fg='black')
btnCE.grid(row=2, column=1, sticky="nsew")

btnC = Button(calc, text="C", font=button_bold_font, bd=4, command=c, bg='lightgray', fg='black')
btnC.grid(row=2, column=2, sticky="nsew")

btnX = Button(calc, text="←", font=button_bold_font, bd=4, command=backspace, bg='lightgray', fg='black')
btnX.grid(row=2, column=3, sticky="nsew")

for i in range(8):
    calc.grid_rowconfigure(i, weight=1)
for j in range(4):
    calc.grid_columnconfigure(j, weight=1)

calc.bind("<Configure>", resize_fonts)
calc.mainloop()
