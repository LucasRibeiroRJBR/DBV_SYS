import customtkinter as ctk
from src import fontes,images
from src.janelas import cadastros_dbv,lista_dbv
import sqlite3



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('850x300')
        self.columnconfigure((0,1,2),weight=1)
        self.rowconfigure(1,weight=1)
        
        self.lb_titulo = ctk.CTkLabel(master=self,text='Sistema de Gerenciamento do Clube',font=fontes.f_titulos())
        
        self.fr_dbvs = ctk.CTkFrame(master=self,corner_radius=12,height=400,fg_color='#282C34')
        self.fr_adm = ctk.CTkFrame(master=self,corner_radius=12,height=400,fg_color='#282C34')
        self.fr_relatorio = ctk.CTkFrame(master=self,corner_radius=12,height=400,fg_color='#282C34')        

        # FRAME DBVs
        self.bt_titulo_dbv = ctk.CTkButton(master=self.fr_dbvs,text='DBV',image=images.user(),fg_color='#008000',
                                           text_color_disabled='#FFFFFF',font=fontes.f_campos(),state='disabled')
        self.bt_add_dbv = ctk.CTkButton(master=self.fr_dbvs,text='Adicionar Desbravador(a)',font=fontes.f_campos(),command=self.abrirCadastroDBV)
        self.bt_listar_dbv = ctk.CTkButton(master=self.fr_dbvs,text='Consultar Desbravador(a)',font=fontes.f_campos(),command=self.abrirListaDBV)
        
        self.bt_titulo_dbv.grid(row=0,column=0,pady=(5,0))
        self.bt_add_dbv.grid(row=1,column=0,padx=15,pady=(15,0))
        self.bt_listar_dbv.grid(row=2,column=0,padx=15,pady=5)

        # FRAME ADM
        self.bt_titulo_adm = ctk.CTkButton(master=self.fr_adm,text='Administrativo',image=images.user(),fg_color='#008000',
                                           text_color_disabled='#FFFFFF',font=fontes.f_campos(),state='disabled')
        self.bt_controle_men = ctk.CTkButton(master=self.fr_adm,text='Controle de Mensalidades',font=fontes.f_campos())
        self.bt_add_men = ctk.CTkButton(master=self.fr_adm,text='Registrar Pagamento Mensalidade',font=fontes.f_campos())

        self.bt_titulo_adm.grid(row=0,column=0,pady=(5,0))
        self.bt_controle_men.grid(row=1,column=0,padx=15,pady=(5,0))
        self.bt_add_men.grid(row=2,column=0,padx=15,pady=(5,0))

        # FRAME RELATORIO
        self.bt_titulo_rel = ctk.CTkButton(master=self.fr_relatorio,text='Relatórios',image=images.user(),fg_color='#008000',
                                           text_color_disabled='#FFFFFF',font=fontes.f_campos(),state='disabled')
        self.bt_add_rel = ctk.CTkButton(master=self.fr_relatorio,text='Mensalidades',font=fontes.f_campos())

        self.bt_titulo_rel.grid(row=0,column=0,pady=(5,0))
        self.bt_add_rel.grid(row=1,column=0,padx=15,pady=15)

        
        # GRIDs
        self.lb_titulo.grid(row=0,columnspan=3,padx=15)
        self.fr_dbvs.grid(row=1,column=0,padx=15,pady=15)
        self.fr_adm.grid(row=1,column=1,padx=15,pady=15)
        self.fr_relatorio.grid(row=1,column=2,padx=15,pady=15)

        self.fr_dbvs.columnconfigure(0,weight=1)
        self.fr_dbvs.rowconfigure((0,1,2,3),weight=1)
        self.fr_adm.columnconfigure(0,weight=1)
        self.fr_adm.rowconfigure((0,1,2,3),weight=1)
        self.fr_relatorio.columnconfigure(0,weight=1)
        self.fr_relatorio.rowconfigure((0,1,2,3),weight=1)

        # TopLevels
        self.w_cadastroDBV = None
        self.w_listaDBV = None

    def abrirCadastroDBV(self):
        if self.w_cadastroDBV is None or not self.w_cadastroDBV.winfo_exists():
            self.w_cadastroDBV = cadastros_dbv.CadastroDBV(self)
        else:
            self.w_cadastroDBV.focus()

    def abrirListaDBV(self):
        if self.w_listaDBV is None or not self.w_listaDBV.winfo_exists():
            self.w_listaDBV = lista_dbv.ListaDBV(self)
        else:
            self.w_listaDBV.focus()

if __name__ == '__main__':
    App().mainloop()

