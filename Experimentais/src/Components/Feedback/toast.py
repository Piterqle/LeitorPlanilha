import customtkinter as ctk

class Feedback:
    def __init__(self, root, mensagem = "Mensagem de feedback", color = "#009600"):
        super().__init__()
        self.root = root
        self.mensagem = mensagem
        self.color = color
    

    def toast(self):
        
        self.start_color = self.color       # Cor original (Verde)
        self.bg_color = self.root.cget("fg_color") # Cor de fundo da janela principal
        
        # Criar o Frame do Toast
        self.toast_frame = ctk.CTkFrame(
            bg_color="transparent",
            master=self.root, 
            fg_color=self.start_color, 
            corner_radius=10
        )
        self.toast_frame.place(relx=0.5, rely=0.1, anchor="center")

        # Label da Mensagem
        self.label = ctk.CTkLabel(self.toast_frame, text=self.mensagem, text_color="white")
        self.label.pack(padx=20, pady=10)

        # Variáveis de controle da animação
        self.fade_steps = 25  # Quantidade de frames da animação
        self.current_step = self.fade_steps
        
        # Inicia o processo de destruição após 2 segundos
        self.root.after(2000, self.fade_out)

    def _get_actual_rgb(self, color):
        """
        Extrai o Hex real mesmo que o CTK retorne nomes ou tuplas de temas.
        """
        # Se a cor for uma lista/tupla (Modo Claro, Modo Escuro), pega a atual
        if isinstance(color, (list, tuple)):
            # Pega a cor baseada no tema atual (0 para claro, 1 para escuro)
            appearance_mode = 0 if ctk.get_appearance_mode() == "Light" else 1
            color = color[appearance_mode]
        
        # Se for "transparent", definimos uma cor padrão de fallback (ex: cinza do CTK)
        if color == "transparent":
            color = "#2b2b2b" 
            
        return color

    def _hex_to_rgb(self, hex_color):
        """Converte hex (#RRGGBB) para tupla (R, G, B) com tratamento de erro."""
        try:
            hex_color = hex_color.lstrip('#')
            # Caso receba um nome de cor em vez de HEX, o int(..., 16) falha
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            # Fallback caso a cor seja um nome como 'green' ou 'transparent'
            # Retorna um cinza escuro padrão ou verde se falhar
            return (43, 43, 43) 

    def fade_out(self):
        if not self.toast_frame.winfo_exists():
            return

        if self.current_step >= 0:
            # Garantimos que as cores iniciais e finais sejam HEX válidos
            clean_start = self._get_actual_rgb(self.start_color)
            clean_bg = self._get_actual_rgb(self.bg_color)
            
            start_rgb = self._hex_to_rgb(clean_start)
            end_rgb = self._hex_to_rgb(clean_bg)

            frac = (self.current_step / self.fade_steps) ** 2

            r = int(end_rgb[0] + (start_rgb[0] - end_rgb[0]) * frac)
            g = int(end_rgb[1] + (start_rgb[1] - end_rgb[1]) * frac)
            b = int(end_rgb[2] + (start_rgb[2] - end_rgb[2]) * frac)

            current_hex = f'#{r:02x}{g:02x}{b:02x}'
            
            self.toast_frame.configure(fg_color=current_hex)

            self.current_step -= 1
            self.root.after(20, self.fade_out)
        else:
            self.toast_frame.destroy()
            
    