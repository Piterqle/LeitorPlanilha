import os
import sys
import json
from tkinter import filedialog
import pandas as pd
from src.Models.alunos import Aluno



def caminho_usuario():
    pasta = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Experimentais")
    os.makedirs(pasta, exist_ok=True)
    return os.path.join(pasta, "caminho.json")


caminho_json = caminho_usuario()

def formatar_data(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, pd.Timestamp):
        return data.strftime("%d/%m/%Y")
    else:
        return 

def openPath(model = False, condition = True):
    print("JSON:", caminho_json)

    if not os.path.exists(caminho_json):
        print("Nenhum caminho encontrado.")
        return None

    try:

        with open(caminho_json, 'r') as f:
            conteudo = f.read()

            if not conteudo.strip():
                print("Nenhum caminho encontrado.")
                return None

            caminho = json.loads(conteudo)
        
        caminho_planilha = caminho.get("Planilha")

        # 🔥 Verifica se o arquivo ainda existe
        if not caminho_planilha or not os.path.exists(caminho_planilha):
            print("Planilha não encontrada.")
            return None


        dados = pd.read_excel(caminho_planilha, sheet_name=None)

        dadosFormatados = []
        sheets = []
        
        for sheet, data in dados.items():
            
            data = data.loc[:, ~data.columns.astype(str).str.contains('^Unnamed')]
            data.dropna(how='all', inplace=True)
                        
            if data.columns.tolist() == ["Nome", "Data da Procura", "Data de Experiência", "Semana","Horário", "Contato", "Status"]:
                if model: 
                    sheets.append(sheet.capitalize()) 
                    pass
                
                for index, row in data.iterrows():
                
                    if condition: 
                        aluno = Aluno(
                            nome=row["Nome"],
                            modalidade=sheet,
                            data_procura=row["Data da Procura"] if isinstance(row["Data da Procura"], str) else row["Data da Procura"].strftime("%d/%m/%Y"),
                            data_experiencia=row["Data de Experiência"] if isinstance(row["Data de Experiência"], str) else row["Data de Experiência"].strftime("%d/%m/%Y"),
                            horario=row["Horário"],
                            numero_telefone=row["Contato"],
                            status=row["Status"],
                            row=index + 2
                        )
                        dadosFormatados.append(aluno)
                    
        if model: return sheets
        return dadosFormatados

    except Exception as e:
        print("Erro ao abrir:", e)
        print("Erro ao carregar planilha.")
        return None



def savePath(self):
    planilha = filedialog.askopenfilename(
        title="Selecionar planilha",
        filetypes=(("Planilha Excel", "*.xlsx"), ("Todos os arquivos", "*.*"))
    )

    if not planilha:
        return

    dados = {
        "Planilha": planilha
    }

    try:
        with open(caminho_json, 'w') as f:
            json.dump(dados, f, indent=4)

        print("Caminho salvo com sucesso!")

    except Exception as e:
        print("Erro ao salvar:", e)