import customtkinter as ctk
import tkinter as tk
from Back import openPath, addAluno
import datetime
from tkcalendar import Calendar, DateEntry
from datetime import datetime

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Leitor de Planilha")
        
        self.dias_pt = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    
        
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Selecione a planilha para começar.")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Clique Aqui", command=lambda: openPath(self=self, next=lambda dados: self.home(dados=dados)))
        self.button.pack(pady=10)
    # Função de Focus
    def on_focus_in(self, event):
        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="#1f6aa5")

    def on_focus_out(self, event):
        if (event.widget.master == self.nameEntry and (event.widget.get() == "" or event.widget.get() == "Digite o nome do aluno") ):
               print("Entrou")
               self.dateNowEntry.delete(0, "end")

        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="gray")

    
    # Função para abrir o calendário
    def open_calendar(self):
        
        self.top = tk.Toplevel(self)
        self.top.title("Selecionar Data")

        self.cal = Calendar(self.top, selectmode="day", date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=20, pady=20)

        btn = ctk.CTkButton(self.top, text="Selecionar", command=self.get_date)
        btn.pack(pady=10)

    
    # Função para obter a data selecionada no calendário
    def get_date(self):

        data = self.cal.get_date()
        self.dateMarkedEntry.delete(0, "end")
        self.dateMarkedEntry.insert(0, data)
        self.top.destroy()

    
    # Função para Modificar a Cor do Status
    def status_color(self, status):
        
        colors = {
            "Matriculado": "#4CAF50",
            "Pendente": "#FFC107",
            "Em Andamento": "#2196F3",
            "Cancelado": "#F44336"
        }

        base_color = colors.get(status, "#808080")
    
        badget = ctk.CTkLabel(self.frameLinhas, 
                            text=status.upper(), 
                            fg_color=base_color, 
                            text_color="white", 
                            corner_radius=20,
                            width=100,
                            height=30,
                            font=("Segoe UI", 12, "bold"))
    
        return badget
    
    # Função para construir a interface da Home
    def home(self, dados):
        for widget in self.winfo_children():
            widget.destroy()

        self.geometry("1200x720")

        # Header
        self.header = ctk.CTkFrame(self, height=80, corner_radius=0)
        self.header.pack(fill="x")

        self.header_label = ctk.CTkLabel(
            self.header,
            text="💃 Escola Maiher Menezes",
            font=("Arial", 22, "bold")
        )
        self.header_label.pack(pady=20)


        self.addContainer = ctk.CTkFrame(self, fg_color="transparent")
        self.addContainer.pack(padx=30, pady=25, fill="x", )

        self.addLabel = ctk.CTkLabel(
            self.addContainer,
            text="➕ Adicionar Aluno Experimental",
            font=("Arial", 15, "bold")
        )
        self.addLabel.pack(anchor="w", pady=(10,20))


        self.entryContainer = ctk.CTkFrame(self.addContainer, )
        self.entryContainer.pack(fill="x")

        # deixa as colunas expandirem
        for i in range(6):
            self.entryContainer.grid_columnconfigure(i, weight=1)


        # Nome do Aluno
        self.nameLabel = ctk.CTkLabel(self.entryContainer, text="Nome do Aluno", font=("Arial", 14) )
        self.nameLabel.grid(row=0, column=0, sticky="w", padx=8, pady=(0,5))

        self.nameEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="Digite o nome do aluno")
        self.nameEntry.grid(row=1, column=0, padx=8, pady=(0,15), sticky="ew")

        self.nameEntry.bind("<FocusIn>", lambda e: (self.on_focus_in(e), self.dateNowEntry.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))))
        self.nameEntry.bind("<FocusOut>", lambda e: self.on_focus_out(e))


        # Modalidade
        self.modalidadeLabel = ctk.CTkLabel(self.entryContainer, text="Modalidade", font=("Arial", 14))
        self.modalidadeLabel.grid(row=0, column=1, sticky="w", padx=8, pady=(0,5))

        self.modalidadeEntry = ctk.CTkComboBox(self.entryContainer, values=["Ballet", "Jazz", "Contemporâneo", "Hip Hop", "Salsa"])
        self.modalidadeEntry.grid(row=1, column=1, padx=8, pady=(0,15), sticky="ew")


        # Data Atual
        self.dateNowLabel = ctk.CTkLabel(self.entryContainer, text="Data Atual", font=("Arial", 14))
        self.dateNowLabel.grid(row=0, column=2, sticky="w", padx=8, pady=(0,5))

        self.dateNowEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="dd/mm/aaaa")
        self.dateNowEntry.grid(row=1, column=2, padx=8, pady=(0,15), sticky="ew")


        # Data Marcada
        self.dateMarkedLabel = ctk.CTkLabel(self.entryContainer, text="Data Marcada", font=("Arial", 14))
        self.dateMarkedLabel.grid(row=0, column=3, sticky="w", padx=8, pady=(0,5))

        self.dateMarkedEntry = ctk.CTkEntry(self.entryContainer)
        self.dateMarkedEntry.grid(row=1, column=3, padx=8, pady=(0,15), sticky="ew")
        
        self.dateMarkedEntry.bind("<Button-1>", lambda e: self.open_calendar())


        # Horário
        self.timeLabel = ctk.CTkLabel(self.entryContainer, text="Horário", font=("Arial", 14))
        self.timeLabel.grid(row=0, column=4, sticky="w", padx=8, pady=(0,5))

        self.timeEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="HH:MM")
        self.timeEntry.grid(row=1, column=4, padx=8, pady=(0,15), sticky="ew")


        # Contato
        self.contactLabel = ctk.CTkLabel(self.entryContainer, text="Contato", font=("Arial", 14))
        self.contactLabel.grid(row=0, column=5, sticky="w", padx=8, pady=(0,5))

        self.contactEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="(xx) xxxxx-xxxx")
        self.contactEntry.grid(row=1, column=5, padx=8, pady=(0,15), sticky="ew")
       
        
        # Status
        self.statusLabel = ctk.CTkLabel(self.entryContainer, text="Status", font=("Arial", 14))
        self.statusLabel.grid(row=0, column=6, sticky="w", padx=8, pady=(0,5))

        self.statusEntry = ctk.CTkComboBox(self.entryContainer, values=["Matriculado", "Pendente", "Em Andamento" ,"Cancelado"])
        self.statusEntry.grid(row=1, column=6, padx=8, pady=(0,15), sticky="ew")
        
        #Focus automático
        self.nameEntry.bind("<Return>", lambda e: (self.modalidadeEntry.focus()))
        self.modalidadeEntry.bind("<Return>", lambda e: self.dateMarkedEntry.focus())
        self.dateMarkedEntry.bind("<Return>", lambda e: self.statusEntry.focus())
        self.statusEntry.bind("<Return>", lambda e: self.contactEntry.focus())
    
        
        self.buttonAdd = ctk.CTkButton(self.addContainer, text="Adicionar Aluno", command=addAluno)
        self.buttonAdd.pack(pady=10, anchor="e")
        
        
        # Frame da Tabela
        self.tableContainer = ctk.CTkFrame(self, fg_color="transparent")
        self.tableContainer.pack(padx=30, pady=25, fill="both", expand=True)
        
        
        #Frame Filtro
        self.frameFiltro = ctk.CTkFrame(self.tableContainer, fg_color="transparent")
        self.frameFiltro.pack(anchor="e", pady=(0,10))
        
        
        # Filtro
        self.filtroLabel = ctk.CTkLabel(self.frameFiltro, text="Filtrar por:", font=("Arial", 16, "bold"))
        self.filtroLabel.pack(anchor="w", pady=(0,10))
        
        self.filtroBox = ctk.CTkComboBox(self.frameFiltro, values=["📅 Hoje", "🕺 Modalidade"] , font=("Arial", 14, "bold"))
        self.filtroBox.pack(anchor="e", pady=(0,10))
        
        
        # Tabela de Alunos
        self.table = ctk.CTkFrame(self.tableContainer, fg_color="transparent")
        self.table.pack(fill="both", expand=True)
        

        # Criando os Headers da Tabela
        self.headers = ["Nome do Aluno", "Modalidade", "Data Atual", "Data Marcada", "Dia da Semana", "Horário", "Contato", "Status"]
          
          
        # Frame Headers
        self.frameHeaders = ctk.CTkFrame(self.table)
        self.frameHeaders.pack(fill="x")
        
        
        # Frame Linhas
        self.frameLinhas = ctk.CTkScrollableFrame(self.table)
        self.frameLinhas.pack(fill="both", expand=True)
        self.frameLinhas._parent_canvas.configure(highlightthickness=0)
        

        for i, header in enumerate(self.headers):
            self.frameHeaders.grid_columnconfigure(i, weight=1, uniform="col")
            self.frameLinhas.grid_columnconfigure(i, weight=1, uniform="col")
        
            label = ctk.CTkLabel(self.frameHeaders, 
                                 text=header, 
                                 font=("Arial", 15, "bold"), 
                                 anchor="w")
            label.grid(row=0, column=i, padx=(15, 5), pady=5, sticky="ew")
        
        self.frameHeaders.grid_columnconfigure(len(self.headers), weight=0, minsize=14) 

        # Crie um label vazio ou frame transparente para ocupar esse espaço
        spacer = ctk.CTkLabel(self.frameHeaders, text="", width=14)
        spacer.grid(row=0, column=len(self.headers))
        

        # Criação de Linhas
        if(len(dados) > 0):
            for sheet_name, rows in dados.items():
                print(f"==== {sheet_name} ====")
                for i, row in enumerate(rows):
                    
                    if row[2].strftime("%d/%m/%Y") == datetime.now().strftime("%d/%m/%Y"):
                        
                        label_nome = ctk.CTkLabel(self.frameLinhas, text=row[0].upper()[:20] + "..." if len(row[0]) > 20 else row[0].upper(), anchor="w")
                        label_nome.grid(row=i, column=0, padx=(15, 5), pady=5, sticky="ew")
                        
                        label_modalidade = ctk.CTkLabel(self.frameLinhas, text=sheet_name, anchor="w")
                        label_modalidade.grid(row=i, column=1, padx=(15, 5), pady=5, sticky="ew")
                        
                        label_dataAtual = ctk.CTkLabel(self.frameLinhas, text=row[1].strftime("%d/%m/%Y"), anchor="w")
                        label_dataAtual.grid(row=i, column=2, padx=(15, 5),  pady=5, sticky="ew")
                        
                        label_dataMarcada = ctk.CTkLabel(self.frameLinhas, text=row[2].strftime("%d/%m/%Y"), anchor="w")
                        label_dataMarcada.grid(row=i, column=3, padx=(15, 5), pady=5, sticky="ew")
                        
                        label_diaSemana = ctk.CTkLabel(self.frameLinhas, text=self.dias_pt[row[2].weekday()], anchor="w")
                        label_diaSemana.grid(row=i, column=4, padx=(15, 5), pady=5, sticky="ew")
                        
                        label_horario = ctk.CTkLabel(self.frameLinhas, text=row[3], anchor="w")
                        label_horario.grid(row=i, column=5, padx=(15, 5), pady=5, sticky="ew") 
                        
                        label_contato = ctk.CTkLabel(self.frameLinhas, text=row[4], anchor="w")
                        label_contato.grid(row=i, column=6, padx=(15, 5), pady=5, sticky="ew")
                    
                        self.status_color(row[5]).grid(row=i, column=7, padx=(15, 5), pady=5, sticky="ew")

        
    

      

        

        

        

        

Janela().mainloop()