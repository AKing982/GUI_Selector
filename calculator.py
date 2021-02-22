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

        # Enter the mainloop
        self.main_window.mainloop()




if __name__ == "__main__":
    gui = CalcGUI()



