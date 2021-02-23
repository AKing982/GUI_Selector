from tkinter import *

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
        self.btn_row5_frame = Frame(self.main_window)
        self.btn_row6_frame = Frame(self.main_window)

        # Create and pack widgets for the entry frame
        calc_label = Label(self.entry_frame, text='')
        user_entry = Entry(self.entry_frame, width=10, borderwidth=5)

        # Pack the widget
        calc_label.pack(side='left')
        user_entry.pack()

        # Create and pack widgets for the first btn row
        recip_btn = Button(self.btn_row1_frame, text="1/x", padx=40, pady=40)
        square_btn= Button(self.btn_row1_frame, text="x^2", padx=40, pady=40)
        clear_btn = Button(self.btn_row1_frame, text="C", padx=40, pady=40)
        division_btn = Button(self.btn_row1_frame, text="/", padx=40, pady=40)

        # Pack the button widgets
        recip_btn.pack(side='left')
        clear_btn.pack(side='left')
        division_btn.pack(side='left')

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


