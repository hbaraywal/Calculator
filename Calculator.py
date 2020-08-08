from tkinter import *
import tkinter as tk

expression = ""

def click(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal(): 
    
    try: 
  
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = str(total)
    except: 
        equation.set("Wrong expression. Try again!") 
        expression = "" 
        
def percent():
    global expression
    total = int(expression) / 100
    equation.set(total)

def addmin():
    global expression

    if int(expression) == 0:
        pass
    elif int(expression) < 0:
        expression = str(expression.replace('-', '+'))
        equation.set(expression)
    else:
        expression = str(expression.replace('+', '-'))
        equation.set(expression)

        
if __name__ == "__main__":
    
    window = tk.Tk()
    window.title("Simple Calculator") 
    window.geometry("215x200")
    window.resizable(0,0)
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation)
    expression_field.grid(columnspan=8, ipadx=7) 
    equation.set('') 
  
    Button(window, text = "AC", width = 2, command = clear).place(x = 5, y = 50) #.grid(row = 100, column = 0, sticky = E)
    Button(window, text = "+/-", width = 2, command = lambda: addmin()).place(x = 55, y = 50)
    Button(window, text = "%", width = 2, command = lambda: percent()).place(x = 105, y = 50)
    Button(window, text = "/", width = 2, command = lambda: click('/')).place(x = 155, y = 50)

    Button(window, text = "7", width = 2, command = lambda: click(7)).place(x = 5, y = 80)
    Button(window, text = "8", width = 2, command = lambda: click(8)).place(x = 55, y = 80)
    Button(window, text = "9", width = 2, command = lambda: click(9)).place(x = 105, y = 80)
    Button(window, text = "X", width = 2, command = lambda: click("*")).place(x = 155, y = 80)

    Button(window, text = "4", width = 2, command = lambda: click(4)).place(x = 5, y = 110)
    Button(window, text = "5", width = 2, command = lambda: click(5)).place(x = 55, y = 110)
    Button(window, text = "6", width = 2, command = lambda: click(6)).place(x = 105, y = 110)
    Button(window, text = "-", width = 2, command = lambda: click("-")).place(x = 155, y = 110)

    Button(window, text = "1", width = 2, command = lambda: click(1)).place(x = 5, y = 140)
    Button(window, text = "2", width = 2, command = lambda: click(2)).place(x = 55, y = 140)
    Button(window, text = "3", width = 2, command = lambda: click(3)).place(x = 105, y = 140)
    Button(window, text = "+", width = 2, command = lambda: click("+")).place(x = 155, y = 140)

    Button(window, text = "0", width = 7, command = lambda: click(0)).place(x = 5, y = 170)
    Button(window, text = ".", width = 2, command = lambda: click(".")).place(x = 105, y = 170)
    Button(window, text = "=", width = 2, command = equal).place(x = 155, y = 170)
    
window.mainloop()
