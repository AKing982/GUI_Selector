from tkinter import *
import sqlite3
import tkinter

class DataGUI:

    def __init__(self):

        self.main_window = Tk()
        self.main_window.title('Records')
        self.main_window.geometry('400x300')

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
        self.delete_frame = Frame(self.main_window)
        self.btn_frame = Frame(self.main_window)
        self.result_frame = Frame(self.main_window)

        self.full_name_entry = Entry(self.name_frame, width=30)
        self.full_name_entry.grid(row=0,column=1)
        self.email_entry = Entry(self.email_frame, width=30)
        self.email_entry.grid(row=1, column=1)
        self.phone_entry = Entry(self.phone_frame, width=30)
        self.phone_entry.grid(row=2, column=1)
        self.zipcode_entry = Entry(self.zipcode_frame, width=30)
        self.zipcode_entry.grid(row=3,column=1)
        self.state_entry = Entry(self.state_frame, width=30)
        self.state_entry.grid(row=4, column=1)
        self.student_entry = Entry(self.student_frame, width=30)
        self.student_entry.grid(row=5,column=1)
        self.delete_entry = Entry(self.delete_frame, width=30)
        self.delete_entry.grid(row=6, column=1)

        # Create TextBox Labels
        self.welcome_label = Label(self.welcome_frame, text='Welcome to Contacts', font='Helvetica 9 bold')
        self.full_name_label = Label(self.name_frame, text="Enter Full Name: ")
        self.full_name_label.grid(row=0, column=0)
        self.email_label = Label(self.email_frame, text="Enter Email: ")
        self.email_label.grid(row=1, column=0)
        self.phone_label = Label(self.phone_frame, text="Enter Phone: ")
        self.phone_label.grid(row=2, column=0)
        self.zip_label = Label(self.zipcode_frame, text="Enter ZipCode: ")
        self.zip_label.grid(row=3, column=0)
        self.state_label = Label(self.state_frame, text='Enter State: ')
        self.state_label.grid(row=4, column=0)
        self.student_label = Label(self.student_frame, text="Enter Y/N if Student: ")
        self.student_label.grid(row=5, column=0)
        self.delete_label = Label(self.delete_frame, text='Delete ID')
        self.delete_label.grid(row=6, column=0)

        # Create a submit button
        self.submit_btn = Button(self.btn_frame, text='Submit', command=self.submit)
        self.submit_btn.grid(row=0, column=1)

        # Create an Edit button
        self.edit_btn = Button(self.btn_frame, text='Edit Record', command=self.edit)
        self.edit_btn.grid(row=0, column=2)

        # Create a delete button
        self.delete_btn = Button(self.btn_frame, text='Delete Record', command=self.delete)
        self.delete_btn.grid(row=0, column=3)

         # Create a query button
        self.query_btn = Button(self.btn_frame,text='Show Record', command=self.query)
        self.query_btn.grid(row=0, column=4)

        # Create a quit button
        self.quit_btn = Button(self.btn_frame, text='Quit', command=self.main_window.destroy)
        self.quit_btn.grid(row=0, column=5)

        # Pack the frames
        self.welcome_frame.pack()
        self.name_frame.pack()
        self.email_frame.pack()
        self.phone_frame.pack()
        self.zipcode_frame.pack()
        self.state_frame.pack()
        self.student_frame.pack()
        self.delete_frame.pack()
        self.btn_frame.pack()
        self.result_frame.pack()

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

        query_label = Label(self.result_frame, text=print_records)
        query_label.grid(row=7, column=0)

        self.conn2.commit()
        self.conn2.close()

    def delete(self):
        # Create a connection
        self.conn3 = sqlite3.connect('contact_books.db')

        # Create a Cursor
        self.c3 = self.conn3.cursor()

        # Delete the record
        self.c3.execute('DELETE FROM contact_books WHERE oid=' + self.delete_entry.get())

        # Commit changes
        self.conn3.commit()

        # Close the connection
        self.conn3.close()

    def update_records(self):
        # Create a connection
        self.conn5 = sqlite3.connect('contact_books.db')

        # Create a cursor
        self.c5 = self.conn5.cursor()

        # Update the record
        self.c5.execute("""UPDATE contact_books SET
                        full_name = :full,
                        email = :email,
                        phone = :phone,
                        zipcode = :zipcode,
                        state = :state,
                        student = :student
                        
                        WHERE oid = :oid""",
                        {
                            'full_name': self.full_name_entry_edit.get(),
                            'email': self.email_entry_edit.get(),
                            'phone': self.phone_entry_edit.get(),
                            'zipcode': self.zipcode_entry_edit.get(),
                            'state': self.state_entry_edit.get(),
                            'student': self.student_entry_edit.get(),
                            'oid': self.record_id
                        })

        # Commit changes
        self.conn5.commit()

        # Close the connection
        self.conn5.close()

    def edit(self):

        self.edit_window = Tk()
        self.edit_window.title('Records')
        self.edit_window.geometry('340x300')


        self.full_name_entry_edit = Entry(self.edit_window, width=30)
        self.full_name_entry_edit.grid(row=0, column=1)
        self.email_entry_edit = Entry(self.edit_window, width=30)
        self.email_entry_edit.grid(row=1, column=1)
        self.phone_entry_edit = Entry(self.edit_window, width=30)
        self.phone_entry_edit.grid(row=2, column=1)
        self.zipcode_entry_edit = Entry(self.edit_window, width=30)
        self.zipcode_entry_edit.grid(row=3, column=1)
        self.state_entry_edit = Entry(self.edit_window, width=30)
        self.state_entry_edit.grid(row=4, column=1)
        self.student_entry_edit = Entry(self.edit_window, width=30)
        self.student_entry_edit.grid(row=5, column=1)
        self.delete_entry_edit = Entry(self.edit_window, width=30)
        self.delete_entry_edit.grid(row=6, column=1)

        # Create TextBox Labels
        self.welcome_label_edit = Label(self.edit_window, text='Welcome to Contacts', font='Helvetica 9 bold')
        self.full_name_label_edit = Label(self.edit_window, text="Enter Full Name: ")
        self.full_name_label_edit.grid(row=0, column=0)
        self.email_label_edit = Label(self.edit_window, text="Enter Email: ")
        self.email_label_edit.grid(row=1, column=0)
        self.phone_label_edit = Label(self.edit_window, text="Enter Phone: ")
        self.phone_label_edit.grid(row=2, column=0)
        self.zip_label_edit = Label(self.edit_window, text="Enter ZipCode: ")
        self.zip_label_edit.grid(row=3, column=0)
        self.state_label_edit = Label(self.edit_window, text='Enter State: ')
        self.state_label_edit.grid(row=4, column=0)
        self.student_label_edit = Label(self.edit_window, text="Enter Y/N if Student: ")
        self.student_label_edit.grid(row=5, column=0)
        self.delete_label_edit = Label(self.edit_window, text='Delete ID')
        self.delete_label_edit.grid(row=6, column=0)

        # Create a Save button
        self.save_btn = Button(self.edit_window, text='Save Record', command=self.edit)
        self.save_btn.grid(row=7, column=1)

        # Create a connection
        self.conn4 = sqlite3.connect('contact_books.db')

        # Create a cursor
        self.c4 = self.conn4.cursor()

        self.record_id = self.delete_entry.get()

        # Update the query
        self.c4.execute('SELECT * FROM contact_books WHERE oid = ' + self.record_id)
        self.records = self.c4.fetchall()

        for record in self.records:
            self.full_name_entry_edit.insert(0, record[0])
            self.email_entry_edit.insert(0, record[1])
            self.phone_entry_edit.insert(0, record[2])
            self.zipcode_entry_edit.insert(0, record[3])
            self.state_entry_edit.insert(0, record[4])
            self.delete_entry_edit.insert(0, record[5])

        # Commit the changes
        self.conn4.commit()

        # Close the connection
        self.conn4.close()


        self.edit_window.mainloop()




if __name__ == '__main__':

    gui = DataGUI()