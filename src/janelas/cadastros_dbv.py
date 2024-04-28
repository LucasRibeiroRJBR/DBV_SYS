import customtkinter as ctk
from src import fontes,images
import sqlite3

class CadastroDBV(ctk.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Cadastro de DBV')
        self.after(100,self.lift)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)

        self.cursor_unidades = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM UNIDADES')
        self.cursor_classes = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM CLASSES')

        self.img_cadastro_dbv = ctk.CTkButton(master=self,text='',image=images.user(),state='disabled',fg_color='#008000')
        self.lb_titulo = ctk.CTkLabel(master=self,text='Cadastro DBV',font=fontes.f_titulos())
        self.fr_formulario = ctk.CTkFrame(master=self,corner_radius=12,fg_color='#282C34')
        self.fr_formulario.columnconfigure((0,1),weight=1)

        self.vSeg = ctk.StringVar(value=0)
        self.vClasse = ctk.StringVar()
        self.vUnidade = ctk.StringVar()

        self.lb_nome = ctk.CTkLabel(master=self.fr_formulario,text='Nome: ',font=fontes.f_campos())
        self.in_nome = ctk.CTkEntry(master=self.fr_formulario,placeholder_text="Digite o nome...",width=500,font=fontes.f_campos())
        self.lb_dt_nasc = ctk.CTkLabel(master=self.fr_formulario,text='Data de Nascimento: ',font=fontes.f_campos())
        self.in_dt_nasc = ctk.CTkEntry(master=self.fr_formulario,placeholder_text="XX/XX/XXXX",width=250,font=fontes.f_campos())
        self.chb_seguro = ctk.CTkCheckBox(master=self.fr_formulario,text=' Seguro pago',variable=self.vSeg,onvalue=1,offvalue=0,font=fontes.f_campos())
        self.lb_classe = ctk.CTkLabel(master=self.fr_formulario,text='Classe: ',font=fontes.f_campos())
        self.opm_classe = ctk.CTkOptionMenu(master=self.fr_formulario, values=[i[1] for i in self.cursor_classes],
                                            font=fontes.f_campos(),dropdown_font=fontes.f_campos(),variable=self.vClasse)
        self.lb_unidade = ctk.CTkLabel(master=self.fr_formulario,text='Unidade: ',font=fontes.f_campos())
        self.opm_unidade = ctk.CTkOptionMenu(master=self.fr_formulario, values=[i[1] for i in self.cursor_unidades],
                                            font=fontes.f_campos(),dropdown_font=fontes.f_campos(),variable=self.vUnidade)
        self.bt_registrar = ctk.CTkButton(master=self.fr_formulario,text='Registrar',font=fontes.f_campos(),
                                          command=lambda: self.registrar(self.in_nome.get(),self.in_dt_nasc.get(),self.vSeg.get(),self.vClasse.get(),self.vUnidade.get()))

        self.img_cadastro_dbv.grid(row=0,column=0,padx=15)
        self.lb_titulo.grid(row=0,column=1,columnspan=2,padx=15,sticky='w')
        self.fr_formulario.grid(row=1,columnspan=2,padx=15,pady=15)
        self.lb_nome.grid(row=0,column=0,padx=(5,0),pady=5,sticky='w')
        self.in_nome.grid(row=0,column=1,padx=(0,5),pady=5,sticky='w')
        self.lb_dt_nasc.grid(row=1,column=0,padx=(5,0),pady=5,sticky='w')
        self.in_dt_nasc.grid(row=1,column=1,padx=(0,5),pady=5,sticky='w')
        self.chb_seguro.grid(row=2,column=1,padx=(0,5),pady=5,sticky='w')
        self.lb_classe.grid(row=3,column=0,padx=(5,0),pady=5,sticky='w')
        self.opm_classe.grid(row=3,column=1,padx=(0,5),pady=5,sticky='w')
        self.lb_unidade.grid(row=4,column=0,padx=(5,0),pady=5,sticky='w')
        self.opm_unidade.grid(row=4,column=1,padx=(0,5),pady=5,sticky='w')
        self.bt_registrar.grid(row=5,columnspan=2,padx=5,pady=5,sticky='nswe')

    def registrar(self,nom,dt,seg,cl,uni):
        match cl:
            case 'Amigo': cl = 1
            case 'Companheiro': cl = 2
            case 'Pesquisador': cl = 3
            case 'Pioneiro': cl = 4
            case 'Excursionista': cl = 5
            case 'Guia': cl = 6
            case 'Líder': cl = 7
            case 'Líder Master': cl = 8
            case 'Líder Master Avançado': cl = 9
        match uni:
            case 'Cães de Caça': uni = 1
            case 'Lynce': uni = 2
            case 'Pégasus': uni = 3
            case 'Diretoria': uni = 4
        self.cursor_registrar = sqlite3.connect('db/DBS_SYS.db')
        self.query_insert = (f"INSERT INTO DBV(NOME, DT_NASC, SEGURO_PG, ID_CLASSE, ID_LIST_ESP, ID_SEGURO, ID_UNIDADE) VALUES (?,?,?,?,?,?,?);")
        self.valores_insert = (nom,dt,seg,cl,None,None,uni)
        self.cursor_registrar.execute(self.query_insert,self.valores_insert)
        self.cursor_registrar.commit()
        self.cursor_registrar.close()  