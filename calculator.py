from tkinter import *
import tkinter

class CalcGUI:
    def __init__(self):

        # Create the main window for our calculator app
        self.main_window = Tk()
        self.main_window.geometry('500x200')
        self.main_window.title('Calculator')

        # Create the Five frames
        self.entry_frame = Frame(self.main_window)
        self.btn_row1_frame = Frame(self.main_window)
        self.btn_row2_frame = Frame(self.main_window)
        self.btn_row3_frame = Frame(self.main_window)
        self.btn_row4_frame = Frame(self.main_window)

        self.calc_entry = Entry(self.entry_frame, width=40, borderwidth=5)
        self.calc_entry.pack(side='left')

        # Create buttons 7, 8, 9, +
        self.btn_7 = Button(self.btn_row1_frame, text='7', width=15, padx=10, pady=10,command=lambda: self.OnClick(7))
        self.btn_8 = Button(self.btn_row1_frame, text='8', width=15, padx=10, pady=10,command=lambda: self.OnClick(8))
        self.btn_9 = Button(self.btn_row1_frame, text='9', width=15, padx=10, pady=10,command=lambda: self.OnClick(9))
        self.btn_plus = Button(self.btn_row1_frame, text='+', width=15, padx=10, pady=10,command=lambda: self.add())

        # Pack the buttons
        self.btn_7.pack(side='left')
        self.btn_8.pack(side='left')
        self.btn_9.pack(side='left')
        self.btn_plus.pack(side='left')

        # Create button's 4, 5, 6, -
        self.btn_4 = Button(self.btn_row2_frame, text='4', width=15, padx=10, pady=10,command=lambda: self.OnClick(4))
        self.btn_5 = Button(self.btn_row2_frame, text='5', width=15, padx=10, pady=10,command=lambda: self.OnClick(5))
        self.btn_6 = Button(self.btn_row2_frame, text='6', width=15, padx=10, pady=10,command=lambda: self.OnClick(6))
        self.btn_minus = Button(self.btn_row2_frame, text='-', width=15, padx=10, pady=10,command=lambda: self.OnClick('-'))

        # Pack the buttons
        self.btn_4.pack(side='left')
        self.btn_5.pack(side='left')
        self.btn_6.pack(side='left')
        self.btn_minus.pack(side='left')

        # Create button's 1, 2, 3, *
        self.btn_1 = Button(self.btn_row3_frame, text='1', width=15, padx=10, pady=10, command=lambda: self.OnClick("1"))
        self.btn_2 = Button(self.btn_row3_frame, text='2', width=15, padx=10, pady=10, command=lambda: self.OnClick(2))
        self.btn_3 = Button(self.btn_row3_frame, text='3', width=15, padx=10, pady=10, command=lambda: self.OnClick(3))
        self.btn_multiply = Button(self.btn_row3_frame, text='*', width=15, padx=10, pady=10,command=lambda: self.OnClick('*'))

        # Pack the buttons
        self.btn_1.pack(side='left')
        self.btn_2.pack(side='left')
        self.btn_3.pack(side='left')
        self.btn_multiply.pack(side='left')

        # Create button's C, 0, =, /
        self.btn_C = Button(self.btn_row4_frame, text='C', width=15, padx=10, pady=10,command=lambda: self.ButtonClear())
        self.btn_zero = Button(self.btn_row4_frame, text='0', width=15, padx=10, pady=10,command=lambda: self.OnClick(0))
        self.btn_equal = Button(self.btn_row4_frame, text='=', width=15, padx=10, pady=10,command=lambda: self.ButtonEqual())
        self.btn_divide = Button(self.btn_row4_frame, text='/', width=15, padx=10, pady=10,command=lambda: self.OnClick('/'))

        # Pack the buttons
        self.btn_C.pack(side='left')
        self.btn_zero.pack(side='left')
        self.btn_equal.pack(side='left')
        self.btn_divide.pack(side='left')

        # Pack the Frames
        self.entry_frame.pack()
        self.btn_row1_frame.pack()
        self.btn_row2_frame.pack()
        self.btn_row3_frame.pack()
        self.btn_row4_frame.pack()

        tkinter.mainloop()

    def OnClick(self, number):
        #self.calc_entry.delete(0, END)
        self.current_num = self.calc_entry.get()
        self.calc_entry.delete(0, END)
        self.calc_entry.insert(0, str(self.current_num) + str(number))

    def ButtonClear(self):
        self.calc_entry.delete(0, END)

    def add(self):
        self.first_num = self.calc_entry.get()
        self.f_num = int(self.first_num)
        self.calc_entry.delete(0, END)
        self.math = 'addition'

    def substract(self):
        self.first_num = self.calc_entry.get()
        self.math = 'subtraction'
        self.f_num = int(self.first_num)
        self.calc_entry.delete(0, END)


    def Divide(self):
        self.first_num = self.calc_entry.get()
        self.math = 'division'
        self.f_num = int(self.first_num)
        self.calc_entry.delete(0, END)

    def Multiply(self):
        # Get the number
        self.first_num = self.calc_entry.get()
        self.math = 'multiplication'
        self.f_num = int(self.first_num)
        self.calc_entry.delete(0, END)

    def ButtonEqual(self):
        self.second_num = self.calc_entry.get()
        self.calc_entry.delete(0, END)

        # If addition is being done
        if self.math == 'addition':
            self.sum = self.f_num + self.first_num
            self.calc_entry.insert(0, self.sum)

        # If subtraction is being done
        elif self.math == 'subtraction':
            self.subtract = self.f_num - self.first_num
            self.calc_entry.insert(0, self.subtract)

        elif self.math == 'multiplication':
            self.multiply = self.f_num * self.first_num
            self.calc_entry.insert(0, self.multiply)

        elif self.math == 'division':
            self.sum = self.f_num / self.first_num
            self.calc_entry.insert(0, self.sum)



if __name__ == '__main__':

    calc = CalcGUI()

