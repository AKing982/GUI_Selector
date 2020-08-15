import tkinter, sqlite3
from tkinter import Frame, Label, Tk, Radiobutton, Toplevel, Entry, Button
import tkinter.messagebox
import database
import mp3_player
import calculator


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
        self.rb1 = Radiobutton(self.mid_frame, text='Contact Book', variable=self.radio_var,value=1, command=self.open_contacts)
        self.rb2 = Radiobutton(self.mid_frame, text='MP3  Player', variable=self.radio_var,value=2, command=self.open_mp3)
        self.rb3 = Radiobutton(self.mid_frame, text='Calculator', variable=self.radio_var, value=3, command=self.open_calc)

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

    def open_contacts(self):
        self.contacts = database.DataGUI().main_window

    # Method for opening mp3 player
    def open_mp3(self):
        self.player = mp3_player.MP3().main_window

    # Method for opening calculator
    def open_calc(self):
        self.calculator = calculator.CalcGUI().main_window



my_gui = GUIApp()