import customtkinter as ctk
from tkinter import messagebox

class TopLevel(ctk.CTkToplevel):
    def __init__(self, root = None, type = "TopLevel", mensagem = "Mensagem de feedback", color = "#009600"):
        super().__init__(root)
        self.root = root
        self.mensagem = mensagem
        self.result = False
        

    def topLevel(self):
        self.geometry("350x200")
        self.title("Feedback")
        self.resizable(False, False)
        self.bell()
        self.protocol("WM_DELETE_WINDOW", lambda: (setattr(self, 'result', False), self.destroy()))
        
        
        self.label = ctk.CTkLabel(self, text=self.mensagem, height=50,text_color="white")
        self.label.pack(padx=20, pady=20)
        
        buttonYes = ctk.CTkButton(self, text="OK", 
                fg_color="#009600", 
                hover_color="#007700",
                width=120,
                command=lambda: (setattr(self, 'result', True), self.destroy())
        )
        buttonYes.pack(pady=10, side="left", padx=(40, 10))
        
        buttonNo = ctk.CTkButton(self, text="Cancelar", 
                fg_color="#ab3027", 
                hover_color="#75201a",
                width=120,
                command=lambda: (setattr(self, 'result', False), self.destroy())
        )
        buttonNo.pack(pady=10, side="right", padx=(10, 40))
        
        self.grab_set()
        self.wait_window()
        