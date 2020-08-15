import tkinter, sqlite3
from tkinter import Frame, Label, Tk, Radiobutton, Toplevel, Entry, Button
import tkinter.messagebox


class GUIApp:
    def __init__(self):
        self.main_window = Tk()

        # Create three frames to use for our radio buttons
        self.welcome_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Create and pack the widgets for our welcome frame
        self.welcome_label = Label(self.welcome_frame, text='Welcome to the GUI App')
        self.welcome_label.pack()

        # Create an IntVar object to use with
        # the RadioButtons
        self.radio_var = tkinter.IntVar()

        # Set the IntVar object to 1
        self.radio_var.set(1)

        # Create the RadioButton widgets in the rb1
        self.rb1 = Radiobutton(self.mid_frame, text='Contact Book', variable=self.radio_var,value=1)
        self.rb2 = Radiobutton(self.mid_frame, text='MP3  Player', variable=self.radio_var,value=2)
        self.rb3 = Radiobutton(self.mid_frame, text='Calculator', variable=self.radio_var, value=3)

        # Pack the radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Pack the frames
        self.welcome_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter mainloop
        tkinter.mainloop()



my_gui = GUIApp()