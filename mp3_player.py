from tkinter import *
import pygame
from tkinter import filedialog

class MP3:
    def __init__(self):
        # Create the main window for our MP3 Player
        self.main_window = Tk()
        self.main_window.title('MP3 Player')
        self.main_window.geometry('1200x900')

        pygame.mixer.init()

        # Create a function that adds songs
        def add_song():
            self.song = filedialog.askopenfilename(initialdir='audio/', title='Choose a song', filetypes=(("mp3 Files", "*.mp3"),
                                                                                                          ))
            self.song_box.insert(END, self.song)

        # Create Playlist Box
        self.song_box = Listbox(self.main_window, bg='black', fg='green', width=60)
        self.song_box.pack(pady=20)

        self.reverse_btn_Img = PhotoImage(file='Reverse.png')
        self.forward_btn_Img = PhotoImage(file='forward.png')
        self.play_btn_Img = PhotoImage(file='Play.png')
        self.pause_btn_Img = PhotoImage(file='Pause.png')
        self.stop_btn_Img = PhotoImage(file='stop.png')

        # Create Player Control Frames
        self.controls_frame = Frame(self.main_window)
        self.controls_frame.pack()

        # Create Player Control Buttons
        self.back_btn = Button(self.controls_frame, image=self.reverse_btn_Img, borderwidth=0)
        self.play_btn = Button(self.controls_frame, image=self.play_btn_Img, borderwidth=0)
        self.forward_btn = Button(self.controls_frame, image=self.forward_btn_Img, borderwidth=0)
        self.pause_btn = Button(self.controls_frame, image=self.pause_btn_Img, borderwidth=0)
        self.stop_btn = Button(self.controls_frame, image=self.stop_btn_Img, borderwidth=0)

        self.back_btn.grid(row=0, column=0)
        self.play_btn.grid(row=0, column=1)
        self.forward_btn.grid(row=0, column=2)
        self.pause_btn.grid(row=0, column=3)
        self.stop_btn.grid(row=0, column=4)

        # Create Menu
        self.menu = Menu(self.main_window)
        self.main_window.config(menu=self.menu)

        # Add Song Menu
        self.add_songs = Menu(self.menu)
        self.menu.add_cascade(label='Add Songs', menu=self.add_songs)
        self.add_songs.add_command(label='Add One Song to PlayList', command=add_song)

        self.main_window.mainloop()

player = MP3()