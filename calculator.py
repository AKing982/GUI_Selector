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
        self.btn_7 = Button(self.btn_row1_frame, text='7', width=15, padx=10, pady=10)
        self.btn_8 = Button(self.btn_row1_frame, text='8', width=15, padx=10, pady=10)
        self.btn_9 = Button(self.btn_row1_frame, text='9', width=15, padx=10, pady=10)
        self.btn_plus = Button(self.btn_row1_frame, text='+', width=15, padx=10, pady=10)

        # Pack the buttons
        self.btn_7.pack(side='left')
        self.btn_8.pack(side='left')
        self.btn_9.pack(side='left')
        self.btn_plus.pack(side='left')

        # Create button's 4, 5, 6, -
        self.btn_4 = Button(self.btn_row2_frame, text='4', width=15, padx=10, pady=10)
        self.btn_5 = Button(self.btn_row2_frame, text='5', width=15, padx=10, pady=10)
        self.btn_6 = Button(self.btn_row2_frame, text='6', width=15, padx=10, pady=10)
        self.btn_minus = Button(self.btn_row2_frame, text='-', width=15, padx=10, pady=10)

        # Pack the buttons
        self.btn_4.pack(side='left')
        self.btn_5.pack(side='left')
        self.btn_6.pack(side='left')
        self.btn_minus.pack(side='left')

        # Create button's 1, 2, 3, *
        self.btn_1 = Button(self.btn_row3_frame, text='1', width=15, padx=10, pady=10)
        self.btn_2 = Button(self.btn_row3_frame, text='2', width=15, padx=10, pady=10)
        self.btn_3 = Button(self.btn_row3_frame, text='3', width=15, padx=10, pady=10)
        self.btn_multiply = Button(self.btn_row3_frame, text='*', width=15, padx=10, pady=10)

        # Pack the buttons
        self.btn_1.pack(side='left')
        self.btn_2.pack(side='left')
        self.btn_3.pack(side='left')
        self.btn_multiply.pack(side='left')

        # Create button's C, 0, =, /
        self.btn_C = Button(self.btn_row4_frame, text='C', width=15, padx=10, pady=10)
        self.btn_zero = Button(self.btn_row4_frame, text='0', width=15, padx=10, pady=10)
        self.btn_equal = Button(self.btn_row4_frame, text='=', width=15, padx=10, pady=10)
        self.btn_divide = Button(self.btn_row4_frame, text='/', width=15, padx=10, pady=10)

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

if __name__ == '__main__':

    calc = CalcGUI()

