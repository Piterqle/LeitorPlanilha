import customtkinter as ctk

class Feedback(ctk.CTk):
    def __init__(self, root, type = "Toast", mensagem = "Mensagem de feedback"):
        super().__init__()
        self.root = root
        self.type = type
        self.mensagem = mensagem
        
    
        
    

    def toast(self):
        self.toast = ctk.CTkFrame(self.root, fg_color="#008000", corner_radius=10)
        self.toast.place(relx=0.5, rely=0.1, anchor="n")
        label = ctk.CTkLabel(self.toast, text=self.mensagem, fg_color="transparent", text_color="#FFFFFF")
        label.pack(padx=20, pady=10)
        self.after(3000, self.destroy)
        
    def animar(self):
        if y > 0.85:
            y -= 0.01
            self.toast.place(relx=0.98, rely=y, anchor="se")
            self.after(10, lambda: self.animar(y))