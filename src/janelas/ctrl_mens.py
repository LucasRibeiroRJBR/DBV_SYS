import customtkinter as ctk
from src import fontes,images
import sqlite3
from CTkTable import *

class ControleMensalidade(ctk.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Controle de Mensalidades')
        self.after(100,self.lift)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)

        cursor_listar_dbv = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM DADOS_DBV')
        cursor_num_rows = sqlite3.connect('db/DBS_SYS.db').execute('SELECT COUNT(0) FROM DBV')

        self.img_cadastro_dbv = ctk.CTkButton(master=self,text='',image=images.user(),state='disabled',fg_color='#008000')
        self.lb_titulo = ctk.CTkLabel(master=self,text='Controle de Mensalidades',font=fontes.f_titulos())
        self.fr_formulario = ctk.CTkFrame(master=self,corner_radius=12,fg_color='#282C34')
        self.fr_formulario.columnconfigure((0,1),weight=1)

        value = [i for i in cursor_listar_dbv]

        self.tb_dbv = CTkTable(master=self.fr_formulario, row=int([i for i in cursor_num_rows][0][0]), column=5, values=value,header_color="green",font=fontes.f_campos(),
                               hover=True,hover_color='#996600')

        self.img_cadastro_dbv.grid(row=0,column=0,padx=15)
        self.lb_titulo.grid(row=0,column=1,columnspan=2,padx=15,sticky='w')
        self.fr_formulario.grid(row=1,columnspan=2,padx=15,pady=15)


        self.tb_dbv.grid(row=0,column=0,columnspan=2,padx=15,pady=15,sticky='nswe')        