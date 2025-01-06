import os
import json

def criar_arquivo(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, "w"):
            print(f"Arquivo {arquivo} foi criado com sucesso")
    else:
        print(f"O arquivo {arquivo} já existe.")
    
def escrever(arquivo, chave, valor):
        dados = {}

        dados[chave] = valor

        with open(arquivo, "w") as f:
             json.dump(dados, f, indent=4)

        print(f"Dados {dados} registrados")


arquivo = "meu_amor.json"
criar_arquivo(arquivo)
escrever(arquivo, "sarah", "Bô")
