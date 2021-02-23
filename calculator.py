from tkinter import *

class CalcGUI:
    def __init__(self):
        # Create the main window for our calculator app
        self.main_window = Tk()
        self.main_window.geometry('500x400')
        self.main_window.title('Calculator')

        # Create the Five frames
        self.entry_frame = Frame(self.main_window)
        self.btn_row1_frame = Frame(self.main_window)
        self.btn_row2_frame = Frame(self.main_window)
        self.btn_row3_frame = Frame(self.main_window)
        self.btn_row4_frame = Frame(self.main_window)
        self.btn_row5_frame = Frame(self.main_window)
        self.btn_row6_frame = Frame(self.main_window)

        # Create and pack widgets for the entry frame
        calc_label = Label(self.entry_frame, text='')
        user_entry = Entry(self.entry_frame, width=90, borderwidth=5)

        # Pack the widget
        calc_label.pack(side='left')
        user_entry.pack()

        # Create and pack widgets for the first btn row
        recip_btn = Button(self.btn_row1_frame, text="1/x", width=15, height=4)
        square_btn= Button(self.btn_row1_frame, text="x^2", width=15, height=4)
        sqrt_btn = Button(self.btn_row1_frame, text="", width=15, height=4)
        division_btn = Button(self.btn_row1_frame, text="/", width=15, height=4)

        # Pack the button widgets
        recip_btn.pack(side='left')
        square_btn.pack(side='left')
        sqrt_btn.pack(side='left')
        division_btn.pack(side='left')

        # Create and pack the widgets for the second btn row
        Button_7 = Button(self.btn_row2_frame, text="7", width=15, height=4)
        Button_8 = Button(self.btn_row2_frame, text="8", width=15, height=4)
        Button_9 = Button(self.btn_row2_frame, text="9", width=15, height=4)
        multi_btn = Button(self.btn_row2_frame, text="*", width=15, height=4)

        # Pack the Button Widgets
        Button_7.pack(side='left')
        Button_8.pack(side='left')
        Button_9.pack(side='left')
        multi_btn.pack(side='left')

        # Create and pack the widgets for the 3rd button row
        Button_4 = Button(self.btn_row3_frame, text="4", width=15, height=4)
        Button_5 = Button(self.btn_row3_frame, text="5", width=15, height=4)
        Button_6 = Button(self.btn_row3_frame, text="6", width=15, height=4)
        subtract_btn = Button(self.btn_row3_frame, text="-", width=15, height=4)

        # Pack the Button Widgets
        Button_4.pack(side='left')
        Button_5.pack(side='left')
        Button_6.pack(side='left')
        subtract_btn.pack(side='left')

        # Create and pack the widgets for the second btn row
        Button_1 = Button(self.btn_row4_frame, text="1", width=15, height=4)
        Button_2 = Button(self.btn_row4_frame, text="2", width=15, height=4)
        Button_3 = Button(self.btn_row4_frame, text="3", width=15, height=4)
        plus_btn = Button(self.btn_row4_frame, text="+", width=15, height=4)

        # Pack the Button Widgets
        Button_1.pack(side='left')
        Button_2.pack(side='left')
        Button_3.pack(side='left')
        plus_btn.pack(side='left')

        # Create and pack the widgets for the second btn row
        Button_0 = Button(self.btn_row5_frame, text="0", width=15, height=4)
        Button_dot = Button(self.btn_row5_frame, text=".", width=15, height=4)
        Button_clear = Button(self.btn_row5_frame, text="C", width=15, height=4)
        Button_equals = Button(self.btn_row5_frame, text="=", width=15, height=4)

        # Pack the Button Widgets
        Button_0.pack(side='left')
        Button_dot.pack(side='left')
        Button_clear.pack(side='left')
        Button_equals.pack(side='left')

        # Pack the Frames
        self.entry_frame.pack()
        self.btn_row1_frame.pack()
        self.btn_row2_frame.pack()
        self.btn_row3_frame.pack()
        self.btn_row4_frame.pack()
        self.btn_row5_frame.pack()
        self.btn_row6_frame.pack()

        # Enter the mainloop
        self.main_window.mainloop()

if __name__ == "__main__":
    gui = CalcGUI()


