import customtkinter
from CTkTable import *
import sqlite3

root = customtkinter.CTk()

cursor_classes = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM DADOS_DBV')
cursor_num_rows = sqlite3.connect('db/DBS_SYS.db').execute('SELECT COUNT(0) FROM DBV')

value = [i for i in cursor_classes]

table = CTkTable(master=root, row=int([i for i in cursor_num_rows][0][0]), column=5, values=value,header_color="green",
                 )

table.grid(row=1,column=0, padx=20, pady=20)


root.mainloop()