from tkinter import ttk
from GUI.Home.Home import Home
import customtkinter as ctk
import tkinter as tk
from Back import openPath, savePath
from tkcalendar import Calendar, DateEntry
from datetime import datetime


class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Leitor de Planilha")
        
        self.geometry("1380x720")
    
        self.dados = openPath(self=self)
        
        
        self.dashboard = ctk.CTkFrame(self, width=230)
        self.dashboard.pack(side="left", fill="y")
        
        self.root = ctk.CTkFrame(self, fg_color="transparent")
        self.root.pack(fill="both", expand=True)
        if self.dados:
            Home(root=self.root, dados=self.dados)
            return 
        
        

        #self.label = ctk.CTkLabel(self, text="Selecione a planilha para começar.")
        #self.label.pack(pady=20)

        #self.button = ctk.CTkButton(self, text="Clique Aqui", command=lambda: (savePath(self=self), self.label.configure(text="Planilha carregada com sucesso!"), self.button.pack_forget(), self.home()))
        #self.button.pack(pady=10)
    
    
    
        

        
    

      

        

        

        

        

Janela().mainloop()