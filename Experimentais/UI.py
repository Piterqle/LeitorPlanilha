import customtkinter as ctk
import tkinter as tk
from Back import openPath
import datetime
from tkcalendar import Calendar, DateEntry

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Leitor de Planilha")
        self.home()
        
        #self.geometry("400x300")

        #self.label = ctk.CTkLabel(self, text="Selecione a planilha para começar.")
        #self.label.pack(pady=20)

        #self.button = ctk.CTkButton(self, text="Clique Aqui", command=lambda: openPath(self=self, next=lambda: self.home()))
        #self.button.pack(pady=10)
        
    def on_focus_in(self, event):
        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="#1f6aa5")

    def on_focus_out(self, event):
        
        if isinstance(event.widget, ctk.CTkEntry):
            event.widget.configure(border_color="gray")

    
    def open_calendar(self):
        
        self.top = tk.Toplevel(self)
        self.top.title("Selecionar Data")

        self.cal = Calendar(self.top, selectmode="day", date_pattern="dd/mm/yyyy")
        self.cal.pack(padx=20, pady=20)

        btn = ctk.CTkButton(self.top, text="Selecionar", command=self.get_date)
        btn.pack(pady=10)

    
    
    
    def get_date(self):

        data = self.cal.get_date()
        self.dateMarkedEntry.delete(0, "end")
        self.dateMarkedEntry.insert(0, data)
        self.top.destroy()

    
    def home(self):
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
            text="➕ Adicionar Aluno",
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

        self.statusEntry = ctk.CTkComboBox(self.entryContainer, values=["Confirmado", "Pendente", "Em Andamento" ,"Cancelado"])
        self.statusEntry.grid(row=1, column=6, padx=8, pady=(0,15), sticky="ew")
        
        #Focus automático
        self.nameEntry.bind("<Return>", lambda e: (self.modalidadeEntry.focus()))
        self.modalidadeEntry.bind("<Return>", lambda e: self.dateMarkedEntry.focus())
        self.dateMarkedEntry.bind("<Return>", lambda e: self.statusEntry.focus())
        self.statusEntry.bind("<Return>", lambda e: self.contactEntry.focus())
    
        
        self.buttonAdd = ctk.CTkButton(self.addContainer, text="Adicionar Aluno",)# command=self.addAluno)
        self.buttonAdd.pack(pady=10, anchor="e")

        
    

      

        

        

        

        

Janela().mainloop()