import customtkinter as ctk
from src import fontes,images,especialidades

class CadastroDBV(ctk.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.after(100,self.lift)
        self.columnconfigure((0,1),weight=1)

        self.lb_titulo = ctk.CTkLabel(master=self,text='Cadastro DBV',font=fontes.f_titulos())
        self.fr_formulario = ctk.CTkFrame(master=self,corner_radius=12,fg_color='#282C34')
        self.fr_formulario.columnconfigure((0,1),weight=1)

        self.vSeg = ctk.StringVar()

        self.lb_nome = ctk.CTkLabel(master=self.fr_formulario,text='Nome: ',font=fontes.f_campos())
        self.in_nome = ctk.CTkEntry(master=self.fr_formulario,placeholder_text="Digite o nome...",width=500,font=fontes.f_campos())
        self.lb_dt_nasc = ctk.CTkLabel(master=self.fr_formulario,text='Data de Nascimento: ',font=fontes.f_campos())
        self.in_dt_nasc = ctk.CTkEntry(master=self.fr_formulario,placeholder_text="XX/XX/XXXX",width=250,font=fontes.f_campos())
        self.chb_seguro = ctk.CTkCheckBox(master=self.fr_formulario,text=' Seguro pago',variable=self.vSeg,onvalue=1,offvalue=0,font=fontes.f_campos())

        self.lb_titulo.grid(row=0,columnspan=2,padx=15)
        self.fr_formulario.grid(row=1,columnspan=2,padx=15,pady=15)
        self.lb_nome.grid(row=0,column=0,padx=(5,0),pady=5,sticky='w')
        self.in_nome.grid(row=0,column=1,padx=(0,5),pady=5,sticky='w')
        self.lb_dt_nasc.grid(row=1,column=0,padx=(5,0),pady=5,sticky='w')
        self.in_dt_nasc.grid(row=1,column=1,padx=(0,5),pady=5,sticky='w')
        self.chb_seguro.grid(row=2,column=1,padx=(0,5),pady=5,sticky='w')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #self.geometry('600x550')
        self.columnconfigure((0,1,2),weight=1)
        
        self.lb_titulo = ctk.CTkLabel(master=self,text='Sistema de Gerenciamento do Clube',font=fontes.f_titulos())
        
        self.fr_dbvs = ctk.CTkFrame(master=self,corner_radius=12,width=200,height=400,fg_color='#282C34')
        self.fr_adm = ctk.CTkFrame(master=self,corner_radius=12,width=200,height=400,fg_color='#282C34')
        self.fr_relatorio = ctk.CTkFrame(master=self,corner_radius=12,width=200,height=400,fg_color='#282C34')        

        # FRAME DBVs
        self.bt_titulo_dbv = ctk.CTkButton(master=self.fr_dbvs,text='DBV',image=images.user(),fg_color='#008000',
                                           text_color_disabled='#FFFFFF',font=fontes.f_campos(),state='disabled')
        self.bt_add_dbv = ctk.CTkButton(master=self.fr_dbvs,text='Adicionar Desbravador(a)',font=fontes.f_campos(),command=self.abrirCadastroDBV)
        self.bt_add_consultar = ctk.CTkButton(master=self.fr_dbvs,text='Consultar Desbravador(a)',font=fontes.f_campos())
        
        self.bt_titulo_dbv.grid(row=0,column=0,pady=(5,0))
        self.bt_add_dbv.grid(row=1,column=0,padx=15,pady=(15,0))
        self.bt_add_consultar.grid(row=2,column=0,padx=15,pady=5)

        # FRAME ADM
        self.bt_titulo_adm = ctk.CTkButton(master=self.fr_adm,text='Administrativo',image=images.user(),fg_color='#008000',
                                           text_color_disabled='#FFFFFF',font=fontes.f_campos(),state='disabled')
        self.bt_add_adm = ctk.CTkButton(master=self.fr_adm,text='Controle de Mensalidades',font=fontes.f_campos())

        self.bt_titulo_adm.grid(row=0,column=0,pady=(5,0))
        self.bt_add_adm.grid(row=1,column=0,padx=15,pady=15)

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

    def abrirCadastroDBV(self):
        if self.w_cadastroDBV is None or not self.w_cadastroDBV.winfo_exists():
            self.w_cadastroDBV = CadastroDBV(self)
        else:
            self.w_cadastroDBV.focus()

if __name__ == '__main__':
    App().mainloop()

