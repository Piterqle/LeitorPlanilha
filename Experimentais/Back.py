import os
from tkinter import filedialog
from flask import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, range_boundaries
from datetime import datetime



def openPath(self):
    if os.path.exists('Experimentais/caminho.json'):
        with open('Experimentais/caminho.json', 'r') as f:
            caminho = f.read()
            if caminho != "":
                
                caminho = json.loads(caminho)
                planilha = pd.ExcelFile(caminho["Planilha"])
                dados = pd.read_excel(caminho["Planilha"], sheet_name=None)
                
                dadosFormatados = []
                for sheet, data in dados.items():
                    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
                    if data.columns.tolist() == ["Aluno", "Data Marcada", "Data de Experiencia", "Horário", "Contato", "Status"]:
                        for linha in data.values.tolist():
                            linha.insert(1, sheet)
                            dadosFormatados.append(linha)
                            
                print(dadosFormatados)
                
                return dadosFormatados
            else:
                self.label.configure(text="Nenhum caminho encontrado.")
                return None
    print('Nenhum caminho encontrado.')
    return None

# Função para salvar o caminho da planilha
def savePath(self):
    
    planilha = filedialog.askopenfilename(
            title="Select a file...",
            filetypes=(("Planilha", "*.xlsx"), ("All files", "*.*"))
    )
    
    with open('Experimentais/caminho.json', 'w') as f:
        f.write('{"Planilha": "' + planilha + '"}')
     
