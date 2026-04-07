from dataclasses import dataclass

# Classe para representar um aluno
@dataclass
class Aluno:
    nome: str
    modalidade: str
    data_marcada: str
    data_experiencia: str
    horario: str
    numero_telefone: str
    status: str
    row: int = None  # Adiciona o atributo row para armazenar a linha do Excel