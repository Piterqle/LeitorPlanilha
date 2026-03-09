import os
from tkinter import filedialog

def openPath(self, next=lambda: None):
    if os.path.exists('Experimentais/caminho.json'):
        with open('Experimentais/caminho.json', 'r') as f:
            caminho = f.read()
            if caminho != "":
                next()
                return
            else:
                self.label.configure(text="Nenhum caminho encontrado.")

    planilha = filedialog.askopenfilename(
            title="Select a file...",
            filetypes=(("Planilha", "*.xlsx"), ("All files", "*.*"))
    )
    with open('Experimentais/caminho.json', 'w') as f:
        f.write('{"Planilha": "' + planilha + '"}')