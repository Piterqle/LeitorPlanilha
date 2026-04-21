import os
import sys
from src.GUI.Home.view import Home
import customtkinter as ctk
from Back import openPath, savePath, caminho_usuario

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

caminho_json = caminho_usuario() 

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Leitor de Planilha")
        #self.iconbitmap(bitmap=resource_path("Assets/Icon/Icon.ico"))
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r') as f:
                conteudo = f.read()

                if conteudo.strip():
                    self.home()
                    return
             
        self.geometry("400x200")
        self.label = ctk.CTkLabel(self, text="Selecione a planilha para começar.")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Clique Aqui", command=lambda: (savePath(self=self), self.label.configure(text="Planilha carregada com sucesso!"), self.button.pack_forget(), self.home()))
        self.button.pack(pady=10)
        return

    
    def home(self):

        self.geometry("1380x720")
        for widget in self.winfo_children():
            widget.destroy()    
        self.dashboard = ctk.CTkFrame(self, width=230)
        self.dashboard.pack(side="left", fill="y")
        self.dashboard.pack_propagate(False)
        
        self.root = ctk.CTkFrame(self, fg_color="transparent")
        self.root.pack(fill="both", expand=True)
        
        self.dashboard_label = ctk.CTkLabel(self.dashboard, text="Dashboard", font=ctk.CTkFont(size=20, weight="bold"))
        self.dashboard_label.pack(pady=10)

        self.button_home = ctk.CTkButton(self.dashboard, text="🏡 Home", font=("Arial", 14),width=200, height=50,fg_color="transparent", hover_color="#333333", command=lambda: Home(root=self.root))
        self.button_home.pack(pady=10, fill="x",)
        

        
    
        

        
    

      

        

        

        

        

Janela().mainloop()