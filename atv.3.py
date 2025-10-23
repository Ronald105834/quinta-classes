import os 
from dataclasses import dataclass
os.system("cls")

@dataclass 
class Pessoa: 
    nome: str 
    idade: str 

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade:")