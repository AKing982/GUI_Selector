import tkinter
from tkinter import *
import sqlite3

def main():

    main_window = Tk()
    main_window.title('Contacts')
    main_window.geometry('400x600')

    # Create a database or connect to it
    conn = sqlite3.connect('contacts.db')

    # Create a cursor
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                Id Integer PRIMARY KEY,
                full_name text,
                email text,
                phone integer,
                zipcode integer,
                student text)''')

    full_name_entry = Entry(main_window, width=30)
    full_name_entry.grid(row=0, column=1)
    email_entry = Entry(main_window, width=30)
    email_entry.grid(row=1, column=1)
    phone_entry = Entry(main_window, width=30)
    phone_entry.grid(row=2, column=1)
    zipcode_entry = Entry(main_window, width=30)
    zipcode_entry.grid(row=3, column=1)
    student_entry = Entry(main_window, width=30)
    student_entry.grid(row=4, column=1)
    delete_entry = Entry(main_window, width=30)
    delete_entry.grid(row=9, column=1)

    # Create TextBox Labels
    full_name_label = Label(main_window, text="Enter Full Name: ")
    full_name_label.grid(row=0, column=0)
    email_label = Label(main_window, text="Enter Email: ")
    email_label.grid(row=1, column=0)
    phone_label = Label(main_window, text="Enter Phone: ")
    phone_label.grid(row=2, column=0)
    zip_label = Label(main_window, text="Enter ZipCode: ")
    zip_label.grid(row=3, column=0)
    student_label = Label(main_window, text="Enter Y/N if Student: ")
    student_label.grid(row=4, column=0)
    delete_label = Label(main_window, text='Delete ID')
    delete_label.grid(row=9, column=0)

    def delete():
        conn3 = sqlite3.connect('contacts.db')

        c3 = conn3.cursor()

        c3.execute("DELETE FROM contacts WHERE oid= " + delete_entry.get())

        conn3.commit()

        conn3.close()

    def update():
        # Create a database connection
        conn5 = sqlite3.connect('contacts.db')

        c5 = conn5.cursor()

        c5.execute("""UPDATE contacts SET 
                   full_name = :full, 
                   email = :email,
                   phone = :phone,
                   zipcode = :zipcode,
                   student = :student

                   WHERE oid = :oid""",
                   {
                       'full': full_name_entry_edit.get(),
                       'email': email_entry_edit.get(),
                       'phone': phone_entry_edit.get(),
                       'zipcode': zipcode_entry_edit.get(),
                       'student': student_entry_edit.get(),

                       'oid': record_id,
                   })

        conn5.commit()

        conn5.close()

        update_window.destroy()

    def edit_records():

        global update_window
        update_window = Tk()
        update_window.title('Update a Record')
        update_window.geometry('400x600')

        # Create global variables
        global full_name_entry_edit
        global email_entry_edit
        global phone_entry_edit
        global zipcode_entry_edit
        global student_entry_edit

        # Create our Text Boxes
        full_name_entry_edit = Entry(update_window, width=30)
        full_name_entry_edit.grid(row=0, column=1)
        email_entry_edit = Entry(update_window, width=30)
        email_entry_edit.grid(row=1, column=1)
        phone_entry_edit = Entry(update_window, width=30)
        phone_entry_edit.grid(row=2, column=1)
        zipcode_entry_edit = Entry(update_window, width=30)
        zipcode_entry_edit.grid(row=3, column=1)
        student_entry_edit = Entry(update_window, width=30)
        student_entry_edit.grid(row=4, column=1)
        delete_entry_edit = Entry(update_window, width=30)
        delete_entry_edit.grid(row=9, column=1)

        # Create textbox labels
        full_name_label = Label(update_window, text="Enter Full Name: ")
        full_name_label.grid(row=0, column=0)
        email_label = Label(update_window, text="Enter Email: ")
        email_label.grid(row=1, column=0)
        phone_label = Label(update_window, text="Enter Phone: ")
        phone_label.grid(row=2, column=0)
        zip_label = Label(update_window, text="Enter ZipCode: ")
        zip_label.grid(row=3, column=0)
        student_label = Label(update_window, text="Enter Y/N if Student: ")
        student_label.grid(row=4, column=0)
        delete_label = Label(update_window, text='Select ID')
        delete_label.grid(row=9, column=0)

        # Create an Update Button
        save_btn = Button(update_window, text='Save Record', command=update)
        save_btn.grid(row=12, column=1, columnspan=2)

        conn4 = sqlite3.connect('contacts.db')

        c4 = conn4.cursor()

        global record_id

        record_id = delete_entry.get()

        c4.execute("SELECT * FROM contacts WHERE oid = " + record_id)
        records = c4.fetchall()
        for record in records:
            full_name_entry_edit.insert(0, record[0])
            email_entry_edit.insert(0, record[1])
            phone_entry_edit.insert(0, record[2])
            zipcode_entry_edit.insert(0, record[3])
            student_entry_edit.insert(0, record[4])
            delete_entry_edit.insert(0, record[5])


    def submit():
        # Create a database or connect to one
        conn1 = sqlite3.connect('contacts.db')

        c1 = conn1.cursor()

        c1.execute("INSERT INTO contacts VALUES (:full_name, :email, :phone, :zipcode, :student)",
                    {
                        'full_name': full_name_entry.get(),
                        'email': email_entry.get(),
                        'phone': phone_entry.get(),
                        'zipcode': zipcode_entry.get(),
                        'student': student_entry.get()
                    })

        conn1.commit()

        conn1.close()

        # Clear TextBoxes
        full_name_entry.delete(0, END)
        email_entry.delete(0, END)
        phone_entry.delete(0, END)
        zipcode_entry.delete(0, END)
        student_entry.delete(0, END)

    # Create Query
    def query():
        conn2 = sqlite3.connect('contacts.db')

        c2 = conn2.cursor()

        c2.execute("SELECT *, oid FROM contacts")
        records = c2.fetchall()
        print(records)

        print_records = ''
        for record in records:
            print_records += str(record) + '\n'

        query_label = Label(main_window, text=print_records)
        query_label.grid(row=13, column=0, columnspan=2)

        conn2.commit()

        conn2.close()

    # Create a submit button
    submit_btn = Button(main_window, text='Submit Record', command=submit)
    submit_btn.grid(row=6, column=1)

    # Create a query button
    query_btn = Button(main_window,text='Show Records', command=query)
    query_btn.grid(row=7, column=1, columnspan=2)

    # Create a Delete Button
    delete_btn = Button(main_window, text='Delete Record', command=delete)
    delete_btn.grid(row=10, column=1, columnspan=2)

    # Create an Update Button
    update_btn = Button(main_window, text='Edit Record', command=edit_records)
    update_btn.grid(row=11, column=1, columnspan=2)

    tkinter.mainloop()

main()