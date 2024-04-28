import customtkinter
from CTkTable import *
import sqlite3

root = customtkinter.CTk()

cursor_classes = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM DBV')

value = [i for i in cursor_classes]

table = CTkTable(master=root, row=15, column=7, values=value)
table.pack(expand=False, fill="both", padx=20, pady=20)

root.mainloop()