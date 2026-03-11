import os
from tkinter import filedialog
from flask import json
import pandas as pd

def openPath(self, next=lambda: None):
    if os.path.exists('Experimentais/caminho.json'):
        with open('Experimentais/caminho.json', 'r') as f:
            caminho = f.read()
            if caminho != "":
                
                caminho = json.loads(caminho)
                planilha = pd.ExcelFile(caminho["Planilha"])
                dados = pd.read_excel(caminho["Planilha"], sheet_name=None)
                
                dados = {sheet: data.values.tolist() for sheet, data in dados.items() if data.columns.tolist() == ["Aluno", "Data Marcada",'Data de Experiencia', 'Horário', 'Contato', 'Status' ]}
                for sheet, data in dados.items():
                    print(f"Dados da planilha '{sheet}':")
                    for row in data:
                        print(row)      
                next(dados=dados)
                return
            else:
                self.label.configure(text="Nenhum caminho encontrado.")

    planilha = filedialog.askopenfilename(
            title="Select a file...",
            filetypes=(("Planilha", "*.xlsx"), ("All files", "*.*"))
    )
    with open('Experimentais/caminho.json', 'w') as f:
        f.write('{"Planilha": "' + planilha + '"}')
        
def addAluno():
    print("Adicionar Aluno")

