import customtkinter as ctk
from src import fontes,images,centralizarJanela
import sqlite3

class RegistroMensalidade(ctk.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Registro de Mensalidades')
        self.after(100,self.lift)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)

        centralizarJanela.centralizar(self)

        self.cursor_unidades = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM UNIDADES')
        self.cursor_classes = sqlite3.connect('db/DBS_SYS.db').execute('SELECT * FROM CLASSES')

        self.img_cadastro_dbv = ctk.CTkButton(master=self,text='',image=images.user(),state='disabled',fg_color='#008000')
        self.lb_titulo = ctk.CTkLabel(master=self,text='Registro de Mensalidade',font=fontes.f_titulos())
        self.fr_formulario = ctk.CTkFrame(master=self,corner_radius=12,fg_color='#282C34')
        self.fr_formulario.columnconfigure((0,1),weight=1)

        self.vClasse = ctk.StringVar()
       
        self.lb_classe = ctk.CTkLabel(master=self.fr_formulario,text='Classe: ',font=fontes.f_campos())
        self.opm_classe = ctk.CTkOptionMenu(master=self.fr_formulario, values=[i[1] for i in self.cursor_classes],
                                            font=fontes.f_campos(),dropdown_font=fontes.f_campos(),variable=self.vClasse)
        
        self.lb_status_registro = ctk.CTkLabel(master=self.fr_formulario,text='')
        self.bt_registrar = ctk.CTkButton(master=self.fr_formulario,text='Registrar',font=fontes.f_campos(),
                                          command=lambda: self.registrar(self.in_nome.get(),self.in_dt_nasc.get(),self.vSeg.get(),self.vClasse.get(),self.vUnidade.get()))

        self.img_cadastro_dbv.grid(row=0,column=0,padx=15)
        self.lb_titulo.grid(row=0,column=1,columnspan=2,padx=15,sticky='w')
        self.fr_formulario.grid(row=1,columnspan=2,padx=15,pady=15)
        self.lb_classe.grid(row=3,column=0,padx=(5,0),pady=5,sticky='w')
        self.opm_classe.grid(row=3,column=1,padx=(0,5),pady=5,sticky='w')
        self.lb_status_registro.grid(row=5,column=0,padx=(0,5),pady=5,sticky='e')
        self.bt_registrar.grid(row=5,column=1,pady=5,sticky='w')

    def registrar(self,nom,dt,seg,cl,uni):
        pass
        try:
            pass
            '''self.cursor_registrar = sqlite3.connect('db/DBS_SYS.db')
            self.query_insert = (f"INSERT INTO DBV(NOME, DT_NASC, SEGURO_PG, ID_CLASSE, ID_LIST_ESP, ID_SEGURO, ID_UNIDADE) VALUES (?,?,?,?,?,?,?);")
            self.valores_insert = (nom,dt,seg,cl,None,None,uni)
            self.cursor_registrar.execute(self.query_insert,self.valores_insert)
            self.cursor_registrar.commit()
            #self.cursor_registrar.close()
            self.lb_status_registro.configure(image=images.registro_ok()) '''
        except Exception as e:
            print(e)
            self.lb_status_registro.configure(image=images.registro_erro()) 
        finally:
            self.in_nome.delete(0,ctk.END)
            self.in_dt_nasc.delete(0,ctk.END)
            self.chb_seguro.deselect()
            self.opm_classe.set('')
            self.opm_unidade.set('')