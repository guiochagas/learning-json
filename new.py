import os
import json

def criar_arquivo(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, "w"):
            print("arquivo criado")
    else:
        print("arquivo já existe.")

def escrever_arquivo(arquivo, chave, valor):
    dado = {}
    dado[chave] = valor
    with open(arquivo, "w") as f:
        json.dump(dado, f, indent=4)

criar_arquivo("sarah.json")
escrever_arquivo("sarah.json", "Sarah", "Caroline")
