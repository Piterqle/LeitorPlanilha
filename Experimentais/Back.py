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


def openPath(self):
    print("JSON:", caminho_json)

    if not os.path.exists(caminho_json):
        print("Nenhum caminho encontrado.")
        return None

    try:

        with open(caminho_json, 'r') as f:
            conteudo = f.read()

            if not conteudo.strip():
                self.label.configure(text="Nenhum caminho encontrado.")
                return None

            caminho = json.loads(conteudo)
        
        caminho_planilha = caminho.get("Planilha")

        # 🔥 Verifica se o arquivo ainda existe
        if not caminho_planilha or not os.path.exists(caminho_planilha):
            self.label.configure(text="Planilha não encontrada.")
            return None


        dados = pd.read_excel(caminho_planilha, sheet_name=None)

        dadosFormatados = []

        for sheet, data in dados.items():
            data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

            if data.columns.tolist() == ["Aluno", "Data Marcada", "Data de Experiencia", "Horário", "Contato", "Status"]:
                for index, row in data.iterrows():
                    aluno = Aluno(
                        nome=row["Aluno"],
                        modalidade=sheet,
                        data_marcada=row["Data Marcada"] if isinstance(row["Data Marcada"], str) else row["Data Marcada"].strftime("%d/%m/%Y"),
                        data_experiencia=row["Data de Experiencia"] if isinstance(row["Data de Experiencia"], str) else row["Data de Experiencia"].strftime("%d/%m/%Y"),
                        horario=row["Horário"],
                        numero_telefone=row["Contato"],
                        status=row["Status"],
                        row=index + 2
                    )
                    dadosFormatados.append(aluno)

        return dadosFormatados

    except Exception as e:
        print("Erro ao abrir:", e)
        self.label.configure(text="Erro ao carregar planilha.")
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