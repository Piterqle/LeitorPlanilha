import customtkinter as ctk
import tkinter as tk
from Back import openPath, savePath
from src.Controllers.alunoController import alunoController
from tkcalendar import Calendar, DateEntry
from datetime import datetime



class Home(ctk.CTk):
    
    def __init__(self, root):
        self.root = root
        self.dados = None
        
        self.dias_pt = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        self.modalidadeList = openPath(model=True)
        self.home()
    
    
    # Função de Focus
    def on_focus_in(self, event):
        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="#1f6aa5")

    def on_focus_out(self, event):
        if (event.widget.master == self.nameEntry and (event.widget.get() == "" or event.widget.get() == "Digite o nome do aluno") ):
               
               self.dateNowEntry.delete(0, "end")

        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="gray")

    
    # Função para abrir o calendário
    def open_calendar(self):
        
        self.top = tk.Toplevel(self.root)
        self.top.title("Selecionar Data")

        self.cal = Calendar(self.top, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, date_pattern="dd/mm/yyyy")
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
            "Matriculado": ["#2a632c", "#6eff74"],
            "Pendente": ["#b38600", "#fcd560"],
            "Andamento": ["#284963", "#5db6fc"],
            "Cancelado": ["#75201a", "#ff7369"]
        }

        base_color = colors.get(status, ["#808080", "white"])
        

        badget = ctk.CTkLabel(self.frameLinhas, 
                            text=status.upper(), 
                            fg_color=base_color[0], 
                            text_color=base_color[1],
                            corner_radius=20,
                            width=90,
                            height=30,
                            font=("Segoe UI", 11, "bold"))
    
        return badget
    
    # Criação de Linhas
    def createRows(self):
        self.dados = openPath(self=self);
        if(len(self.dados) > 0):
            for i, row in enumerate(self.dados):
                #if row[2].strftime("%d/%m/%Y") == datetime.now().strftime("%d/%m/%Y"):
                linha = i * 2
                
                label_Id = ctk.CTkLabel(self.frameLinhas, text=i+1)
                label_Id.grid(row=linha, column=0, padx=(15, 5), pady=5, sticky="ew")
                
                label_nome = ctk.CTkLabel(self.frameLinhas, text=row.nome.upper()[:20] + "..." if len(row.nome) > 20 else row.nome.upper(), anchor="w")
                label_nome.grid(row=linha, column=1, padx=(15, 5), pady=5, sticky="ew")
                
                label_modalidade = ctk.CTkLabel(self.frameLinhas, text=row.modalidade.capitalize(), anchor="w")
                label_modalidade.grid(row=linha, column=2, padx=(15, 5), pady=5, sticky="ew")
                
                # Verificando se row[2] é datetime ou string
                label_dataAtual = ctk.CTkLabel(self.frameLinhas, text=row.data_marcada, anchor="w")
                label_dataAtual.grid(row=linha, column=3, padx=(15, 5),  pady=5, sticky="ew")
                
                # Verificando se row[3] é datetime ou string
                label_dataMarcada = ctk.CTkLabel(self.frameLinhas, text=row.data_experiencia, anchor="w")
                label_dataMarcada.grid(row=linha, column=4, padx=(15, 5), pady=5, sticky="ew")
                
                # Label para o dia da semana, verificando se row[2] é datetime ou string
                label_diaSemana = ctk.CTkLabel(self.frameLinhas, text=self.dias_pt[row.data_experiencia.weekday()] if isinstance(row.data_experiencia, datetime) else self.dias_pt[datetime.strptime(row.data_experiencia, "%d/%m/%Y").weekday()], anchor="w")
                label_diaSemana.grid(row=linha, column=5, padx=(15, 5), pady=5, sticky="ew")
                
                label_horario = ctk.CTkLabel(self.frameLinhas, text=row.horario, anchor="w")
                label_horario.grid(row=linha, column=6, padx=(15, 5), pady=5, sticky="ew") 
                
                label_contato = ctk.CTkLabel(self.frameLinhas, text=row.numero_telefone, anchor="w")
                label_contato.grid(row=linha, column=7, padx=(15, 5), pady=5, sticky="ew")
            
                self.status_color(row.status).grid(row=linha, column=8, padx=(15, 5), pady=5, sticky="ew")
                
                seperator = ctk.CTkFrame(self.frameLinhas, height=1, bg_color="gray", fg_color="white")
                seperator.grid(row=linha+1, column=0, columnspan=9, sticky="ew", padx=10, pady=(0,9))
    
    # Função para construir a interface da Home
    def home(self):
        

        # Header
        self.header = ctk.CTkFrame(self.root, height=50, fg_color="transparent", border_width=1, corner_radius=0)
        self.header.pack(fill="x")

        self.header_label = ctk.CTkLabel(
            self.header,
            text="Planilha Alunos Experimentais",
            font=("Arial", 22, "bold")
        )
        self.header_label.pack(pady=10, padx=20 , anchor="w")


        self.addContainer = ctk.CTkFrame(self.root, fg_color="transparent")
        self.addContainer.pack(padx=30, pady=10 , fill="x", )

        self.addLabel = ctk.CTkLabel(
            self.addContainer,
            text="➕ Adicionar Aluno Experimental",
            font=("Arial", 15, "bold")
        )
        self.addLabel.pack(anchor="w", pady=(10,20))


        self.entryContainer = ctk.CTkFrame(self.addContainer, )
        self.entryContainer.pack(fill="x")

        # deixa as colunas expandirem
        for i in range(5):
            self.entryContainer.grid_columnconfigure(i, weight=1)


        # Nome do Aluno
        self.nameLabel = ctk.CTkLabel(self.entryContainer, text="Nome do Aluno", font=("Arial", 14) )
        self.nameLabel.grid(row=0, column=0, sticky="w", padx=8, pady=(0,5))

        self.nameEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="Digite o nome do aluno", height=30, width=50)
        self.nameEntry.grid(row=1, column=0, padx=8, pady=(0,15), sticky="ew")

        self.nameEntry.bind("<FocusIn>", lambda e: (self.on_focus_in(e), self.dateNowEntry.insert(0, datetime.now().strftime("%d/%m/%Y")) if self.dateNowEntry.get() == "" else ""))
        self.nameEntry.bind("<FocusOut>", lambda e: self.on_focus_out(e))


        # Modalidade
        self.modalidadeLabel = ctk.CTkLabel(self.entryContainer, text="Modalidade", font=("Arial", 14))
        self.modalidadeLabel.grid(row=0, column=1, sticky="w", padx=8, pady=(0,5))

        self.modalidadeEntry = ctk.CTkComboBox(self.entryContainer, values=self.modalidadeList,  height=30)
        self.modalidadeEntry.grid(row=1, column=1, padx=8, pady=(0,15), sticky="ew")


        # Data Atual
        self.dateNowLabel = ctk.CTkLabel(self.entryContainer, text="Data Atual", font=("Arial", 14),  height=30)
        self.dateNowLabel.grid(row=0, column=2, sticky="w", padx=8, pady=(0,5))

        self.dateNowEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="dd/mm/aaaa", height=30)
        self.dateNowEntry.grid(row=1, column=2, padx=8, pady=(0,15), sticky="ew")


        # Data Marcada
        self.dateMarkedLabel = ctk.CTkLabel(self.entryContainer, text="Data Marcada", font=("Arial", 14))
        self.dateMarkedLabel.grid(row=0, column=3, sticky="w", padx=8, pady=(0,5))

        self.dateMarkedEntry = ctk.CTkEntry(self.entryContainer, height=30)
        self.dateMarkedEntry.grid(row=1, column=3, padx=8, pady=(0,15), sticky="ew",  )
        
        self.dateMarkedEntry.bind("<Button-1>", lambda e: self.open_calendar())


        # Horário
        self.timeLabel = ctk.CTkLabel(self.entryContainer, text="Horário", font=("Arial", 14))
        self.timeLabel.grid(row=2, column=0, sticky="w", padx=8, pady=(0,5))

        self.timeEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="HH:MM",  height=30)
        self.timeEntry.grid(row=3, column=0, padx=8, pady=(0,15), sticky="ew")


        # Contato
        self.contactLabel = ctk.CTkLabel(self.entryContainer, text="Contato", font=("Arial", 14))
        self.contactLabel.grid(row=2, column=1, sticky="w", padx=8, pady=(0,5))

        self.contactEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="(xx) xxxxx-xxxx",  height=30)
        self.contactEntry.grid(row=3, column=1, padx=8, pady=(0,15), sticky="ew")
       
        
        # Status
        self.statusLabel = ctk.CTkLabel(self.entryContainer, text="Status", font=("Arial", 14))
        self.statusLabel.grid(row=2, column=2, sticky="w", padx=8, pady=(0,5))

        self.statusEntry = ctk.CTkComboBox(self.entryContainer, values=["Matriculado", "Pendente", "Andamento" ,"Cancelado"], height=30)
        self.statusEntry.grid(row=3, column=2, padx=8, pady=(0,15), sticky="ew")
        
        #Focus automático
        self.nameEntry.bind("<Return>", lambda e: (self.modalidadeEntry.focus()))
        self.modalidadeEntry.bind("<Return>", lambda e: (self.dateMarkedEntry.focus(), self.open_calendar()))
        self.dateNowEntry.bind("<<NotebookTabChanged>>", lambda e:self.open_calendar())
        self.dateMarkedEntry.bind("<Return>", lambda e: self.statusEntry.focus())
        self.statusEntry.bind("<Return>", lambda e: self.contactEntry.focus())
    
        
        self.buttonAdd = ctk.CTkButton(self.entryContainer, text="Adicionar Aluno", height=30, command=lambda: alunoController(
            entrys=[
                self.nameEntry,
                self.modalidadeEntry,
                self.dateNowEntry,
                self.dateMarkedEntry,
                self.timeEntry,
                self.contactEntry,
                self.statusEntry
            ],
            next=self.createRows
        ).addAluno())
        self.buttonAdd.grid(row=3, column=3, padx=8, pady=(0,15), sticky="ew")
        
        # Separador do Edit
        seperator = ctk.CTkFrame(self.entryContainer, height=1, bg_color="gray", fg_color="white")
        seperator.grid(row=4, column=0, columnspan=9, sticky="ew", padx=10, pady=(0,9))
    
        self.buttonAdd.grid(row=3, column=3, padx=8, pady=(0,15), sticky="ew")
        
        # Separador do Edit
        seperator = ctk.CTkFrame(self.entryContainer, height=1, bg_color="gray", fg_color="white")
        seperator.grid(row=4, column=0, columnspan=9, sticky="ew", padx=10, pady=(0,9))
     
        
        # Label do ID     
        self.IdLabel = ctk.CTkLabel(self.entryContainer, text="ID do Aluno")
        self.IdLabel.grid(row=5, column=0, padx=8, pady=(0,5), sticky="w", )
        
        
        # Entry ID para Edit/Delete
        self.IdEntry = ctk.CTkEntry(self.entryContainer, placeholder_text="Digite o ID", height=30)
        self.IdEntry.grid(row=6, column=0, padx=8, pady=(0,15), sticky="ew")
        
        
        entryList = [self.nameEntry,
            self.modalidadeEntry,
            self.dateNowEntry,
            self.dateMarkedEntry,
            self.timeEntry,
            self.contactEntry,
            self.statusEntry]
        
        
        # Button Edit 
        self.buttonEdit = ctk.CTkButton(self.entryContainer, text="Editar Aluno", height=30, fg_color="#d4b350", hover_color="#b38600", command=lambda: alunoController(dados=self.dados, id=self.IdEntry.get(), entrys=entryList, buttons=listButtons, next=self.createRows).editarAluno())
        self.buttonEdit.grid(row=6, column=1, padx=8, pady=(0,15), sticky="ew")
        
        
        # Button Delete 
        self.buttonDelete = ctk.CTkButton(self.entryContainer, text="Deletar Aluno", height=30, fg_color="#ab3027", hover_color="#75201a", command=lambda: alunoController(dados=self.dados, id=self.IdEntry.get(), next=self.createRows).deletarAluno())
        self.buttonDelete.grid(row=6, column=2, padx=8, pady=(0,15), sticky="ew")
           
        listButtons = [self.buttonEdit, self.buttonDelete]
        
        # Frame da Tabela
        self.tableContainer = ctk.CTkFrame(self.root, fg_color="transparent")
        self.tableContainer.pack(padx=30, pady=25, fill="both", expand=True)
        
        
        # Frame Filtro
        self.frameFiltro = ctk.CTkFrame(self.tableContainer, fg_color="transparent", border_width=2, border_color="gray")
        self.frameFiltro.pack(anchor="e", pady=(0,10))
        
        
        # Filtro
        self.filtroLabel = ctk.CTkLabel(self.frameFiltro, text="Filtrar por:", font=("Arial", 16, "bold"))
        self.filtroLabel.grid(column=0, row=0,  padx=10 , pady=(10,10))
        
        self.filtroBox = ctk.CTkComboBox(self.frameFiltro, values=["📅 Hoje", "🕺 Modalidade"] , font=("Arial", 14, "bold"))
        self.filtroBox.grid(column=1, row=0, padx=10, pady=(10,10))
        
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
        

        self.frameHeaders.grid_columnconfigure(0, weight=0, minsize=10) 
        label = ctk.CTkLabel(self.frameHeaders, 
                                text="ID", 
                                font=("Arial", 15, "bold"), 
                                anchor="w",
                                width=14,)
        label.grid(row=0, column=0, padx=(15, 5), pady=5, sticky="ew")
        
        for i, header in enumerate(self.headers):
            self.frameHeaders.grid_columnconfigure(i+1, weight=1, uniform="col")
            self.frameLinhas.grid_columnconfigure(i+1, weight=1, uniform="col")
        
            label = ctk.CTkLabel(self.frameHeaders, 
                                 text=header, 
                                 font=("Arial", 15, "bold"), 
                                 anchor="w")
            label.grid(row=0, column=i+1, padx=(15, 5), pady=5, sticky="ew")
        
        self.frameHeaders.grid_columnconfigure(len(self.headers)+1, weight=0, minsize=14) 

        # Crie um label vazio ou frame transparente para ocupar esse espaço
        spacer = ctk.CTkLabel(self.frameHeaders, text="", width=14)
        spacer.grid(row=0, column=len(self.headers)+1)
        
        self.createRows()

