from tkinter import *
from tkinter import messagebox

WINDOW_POSITION = (600, 200)
OPERATIONS = {'+': lambda a, b: a + b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b,
              '/': lambda a, b: a / b,}


class Calculator:

    def __init__(self):  
        self.left_operand = 0
        self.notation = ''
        
        self.root = Tk()
        self.root.title('Calculator')
        self.root.config(padx=5, pady=5)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.geometry("+%d+%d" % WINDOW_POSITION)

        self.input_field = Entry(self.root, width=22, font='Arial 24')
        self.input_field.grid(row=0, column=0, columnspan=4, sticky=E+W)

        self.btn_1 = Button(self.root, text=1, pady=10, command=lambda: self.number(1))
        self.btn_1.grid(row=2, column=0, sticky=E+W)
        self.btn_2 = Button(self.root, text=2, pady=10, command=lambda:self.number(2))
        self.btn_2.grid(row=2, column=1, sticky=E+W)
        self.btn_3 = Button(self.root, text=3, pady=10, command=lambda:self.number(3))
        self.btn_3.grid(row=2, column=2, sticky=E+W)
        self.btn_4 = Button(self.root, text=4, pady=10, command=lambda:self.number(4))
        self.btn_4.grid(row=3, column=0, sticky=E+W)
        self.btn_5 = Button(self.root, text=5, pady=10, command=lambda:self.number(5))
        self.btn_5.grid(row=3, column=1, sticky=E+W)
        self.btn_6 = Button(self.root, text=6, pady=10, command=lambda:self.number(6))
        self.btn_6.grid(row=3, column=2, sticky=E+W)
        self.btn_7 = Button(self.root, text=7, pady=10, command=lambda:self.number(7))
        self.btn_7.grid(row=4, column=0, sticky=E+W)
        self.btn_8 = Button(self.root, text=8, pady=10, command=lambda:self.number(8))
        self.btn_8.grid(row=4, column=1, sticky=E+W)
        self.btn_9 = Button(self.root, text=9, pady=10, command=lambda:self.number(9))
        self.btn_9.grid(row=4, column=2, sticky=E+W)
        self.btn_0 = Button(self.root, text=0, pady=10, command=lambda:self.number(0))
        self.btn_0.grid(row=5, column=0, columnspan=2, sticky=E+W)

        self.btn_clear = Button(self.root, text='C', pady=10, command=self.clear)
        self.btn_clear.grid(row=1, column=0, sticky=E+W)
        self.btn_negative = Button(self.root, text="+/-", pady=10, command=self.change_sign)
        self.btn_negative.grid(row=1, column=1, sticky=E+W)
        self.btn_percent = Button(self.root, text="%", pady=10, command=self.percentage)
        self.btn_percent.grid(row=1, column=2, sticky=E+W)
        self.btn_divide = Button(self.root, text='/', pady=10, command=lambda:self.operation('/'))
        self.btn_divide.grid(row=1, column=3, sticky=E+W)
        self.btn_multiply = Button(self.root, text='*', pady=10, command=lambda:self.operation('*'))
        self.btn_multiply.grid(row=2, column=3, sticky=E+W)
        self.btn_subtract = Button(self.root, text='-', pady=10, command=lambda:self.operation('-'))
        self.btn_subtract.grid(row=3, column=3, sticky=E+W)
        self.btn_add = Button(self.root, text='+', pady=10, command=lambda:self.operation("+"))
        self.btn_add.grid(row=4, column=3, sticky=E+W)
        self.btn_equals = Button(self.root, text='=', pady=10, command=self.calculate)
        self.btn_equals.grid(row=5, column=3, sticky=E+W)
        self.btn_period = Button(self.root, text='.', pady=10, command=self.decimal_point)
        self.btn_period.grid(row=5, column=2, sticky=E+W)

        self.root.mainloop()

    def clear(self):
        self.input_field.delete(0, END)
        self.notation = ''

    def change_sign(self):
        if self.input_field.get() and not self.input_field.get().startswith('-'):
            value = '-' + self.input_field.get()
        else:
            value = self.input_field.get()[1:]
        
        self.input_field.delete(0, END)
        self.input_field.insert(0, value)

    def percentage(self):
        if self.input_field.get():
            value = eval(self.input_field.get()) / 100
            self.input_field.delete(0, END)
            self.input_field.insert(0, value)
        
    def number(self, number):
        value = self.input_field.get() + str(number)
        self.input_field.delete(0, END)
        self.input_field.insert(0, value)

    def decimal_point(self):
        value = self.input_field.get()

        if value and not '.' in value:
            value += '.'
        else:
            value = '0.'

        self.input_field.delete(0, END)
        self.input_field.insert(0, value)

    def operation(self, sign):
        if not self.left_operand and not self.input_field.get():
            return
        elif self.notation and self.left_operand:
            self.notation = sign
        else:
            self.notation = sign
            self.left_operand = eval(self.input_field.get())
            self.input_field.delete(0, END)

    def calculate(self):
        if not self.notation:
            return
        elif self.input_field.get() and self.left_operand:
            right_operand = eval(self.input_field.get())
        elif self.left_operand:
            right_operand = self.left_operand

        self.input_field.delete(0, END)
        
        try:
            result = OPERATIONS[self.notation](self.left_operand, right_operand)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Zero Division Error")
            self.input_field.delete(0, END)
            return

        if not result % 1:
            result = int(result)

        self.input_field.insert(0, str(result))
        self.left_operand = 0
        self.notation = ''


if __name__ == "__main__":
    calculator = Calculator()