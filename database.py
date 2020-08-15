from tkinter import *
import sqlite3
import tkinter

class DataGUI:

    def __init__(self):

        self.main_window = Tk()

        # Create a database or connect to it
        self.conn = sqlite3.connect('contact_books.db')

        # Create a cursor
        self.c = self.conn.cursor()

    # Create table
        self.c.execute('''CREATE TABLE IF NOT EXISTS contact_books (
                 full_name text,
                 email text,
                 phone integer,
                 zipcode integer,
                 state text,
                 student text)''')

        # Add frames for each of the below variables
        self.welcome_frame = Frame(self.main_window)
        self.name_frame = Frame(self.main_window)
        self.email_frame = Frame(self.main_window)
        self.phone_frame = Frame(self.main_window)
        self.zipcode_frame = Frame(self.main_window)
        self.state_frame = Frame(self.main_window)
        self.student_frame = Frame(self.main_window)
        self.submit_frame = Frame(self.main_window)
        self.query_frame = Frame(self.main_window)

        self.full_name_entry = Entry(self.name_frame, width=30)
        self.email_entry = Entry(self.email_frame, width=30)
        self.phone_entry = Entry(self.phone_frame, width=30)
        self.zipcode_entry = Entry(self.zipcode_frame, width=30)
        self.state_entry = Entry(self.state_frame, width=30)
        self.student_entry = Entry(self.student_frame, width=30)

        # Create TextBox Labels
        self.welcome_label = Label(self.welcome_frame, text='Welcome to Contacts', font='Helvetica 9 bold')
        self.full_name_label = Label(self.name_frame, text="Enter Full Name: ")
        self.email_label = Label(self.email_frame, text="Enter Email: ")
        self.phone_label = Label(self.phone_frame, text="Enter Phone: ")
        self.zip_label = Label(self.zipcode_frame, text="Enter ZipCode: ")
        self.state_label = Label(self.state_frame, text='Enter State: ')
        self.student_label = Label(self.student_frame, text="Enter Y/N if Student: ")

        # Create a submit button
        self.submit_btn = Button(self.submit_frame, text='Submit Record', command=self.submit)

         # Create a query button
        self.query_btn = Button(self.query_frame,text='Show Records', command=self.query)

        # Pack the labels and the Buttons
        self.welcome_label.pack()
        self.full_name_label.pack(side='left')
        self.email_label.pack(side='left')
        self.phone_label.pack(side='left')
        self.zip_label.pack(side='left')
        self.state_label.pack(side='left')
        self.student_label.pack(side='left')
        self.submit_btn.pack(side='left')
        self.query_btn.pack(side='left')

        # Pack the entry's
        self.full_name_entry.pack(side='right')
        self.email_entry.pack(side='right')
        self.phone_entry.pack(side='right')
        self.zipcode_entry.pack(side='right')
        self.state_entry.pack(side='right')
        self.student_entry.pack(side='right')

        # Pack the frames
        self.welcome_frame.pack()
        self.name_frame.pack()
        self.email_frame.pack()
        self.phone_frame.pack()
        self.zipcode_frame.pack()
        self.state_frame.pack()
        self.student_frame.pack()
        self.submit_frame.pack(side='left')
        self.query_frame.pack(side='right')

        tkinter.mainloop()

    def submit(self):
        # Create a database or connect to one
        self.conn1 = sqlite3.connect('contact_books.db')

        self.c1 = self.conn1.cursor()

        # Create table
        self.c1.execute('''CREATE TABLE IF NOT EXISTS contact_books (
                         full_name text,
                         email text,
                        phone integer,
                         zipcode integer,
                         state text,
                         student text)''')

        self.c1.execute("INSERT INTO contact_books VALUES (:full_name, :email, :phone, :zipcode, :state, :student)",
                    {
                        'full_name': self.full_name_entry.get(),
                        'email': self.email_entry.get(),
                        'phone': self.phone_entry.get(),
                        'zipcode': self.zipcode_entry.get(),
                        'state': self.state_entry.get(),
                        'student': self.student_entry.get()
                    }
                    )

        self.conn1.commit()

        # Create Query
    def query(self):
        self.conn2 = sqlite3.connect('contact_books.db')

        self.c2 = self.conn2.cursor()

        self.c2.execute("SELECT *, oid FROM contact_books")
        records = self.c2.fetchall()
        print(records)

        print_records = ''
        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(self.main_window, text=print_records)
        query_label.grid(row=8, column=1, columnspan=2)

        self.conn2.commit()
        self.conn2.close()


        # Close the connection

if __name__ == '__main__':

    gui = DataGUI()