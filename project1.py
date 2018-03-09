from tkinter import *
import sqlite3
conn = sqlite3.connect('phone.db')
curse = conn.cursor()
main = Tk()
main.geometry("298x323")
def create_table():
    curse.execute('CREATE TABLE IF NOT EXISTS phone(name TEXT, number REAL)')
create_table()
name_entry = Entry(main)
name_entry.grid(row=1,column=5)

main.mainloop()
