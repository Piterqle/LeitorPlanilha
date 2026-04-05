import os
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
        
        if not os.path.exists('Experimentais/caminho.json'):  
            self.geometry("400x200")
            self.label = ctk.CTkLabel(self, text="Selecione a planilha para começar.")
            self.label.pack(pady=20)

            self.button = ctk.CTkButton(self, text="Clique Aqui", command=lambda: (savePath(self=self), self.label.configure(text="Planilha carregada com sucesso!"), self.button.pack_forget(), self.home()))
            self.button.pack(pady=10)
            return
        self.home()

    
    def home(self):

        self.geometry("1380x720")
        for widget in self.winfo_children():
            widget.destroy()    
        self.dashboard = ctk.CTkFrame(self, width=230)
        self.dashboard.pack(side="left", fill="y")
        
        self.root = ctk.CTkFrame(self, fg_color="transparent")
        self.root.pack(fill="both", expand=True)
        Home(root=self.root)
    
        

        
    

      

        

        

        

        

Janela().mainloop()