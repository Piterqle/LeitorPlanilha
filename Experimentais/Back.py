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
                
                dados = {sheet: data.values.tolist() for sheet, data in dados.items() if data.columns.tolist() == ["Aluno", "Data Marcada",'Data de Experiencia', 'Horário', 'Contato', 'Status' ]}

                return dados
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
     
def addAluno(aluno, modalidade, data_marcada, data_experiencia, horario, contato, status, next):
    try:
        
        if([aluno, modalidade, data_marcada, data_experiencia, horario, contato, status].count("") > 0):
            print("Preencha todos os campos.")
            return
        
        if(datetime.strptime(data_marcada, "%d/%m/%Y") < datetime.now()):
            print("A data marcada não pode ser anterior à data atual.")
            return

        with open('Experimentais/caminho.json', 'r') as f:
            caminho = f.read()
            if caminho != "":
                caminho = json.loads(caminho)
                
                workbook = load_workbook(caminho["Planilha"])
                worksheet = workbook[modalidade.upper()]
                
                new_row = [aluno, data_marcada, data_experiencia, horario, contato, status]
                worksheet.append(new_row)
                
                if worksheet.tables:
                    table = list(worksheet.tables.values())[0]
                    table.ref = f"A1:F{worksheet.max_row}"

                workbook.save(caminho["Planilha"])
                next()
                
    except Exception as e:
        
        print("Erro ao adicionar aluno:", e)
        return
    
