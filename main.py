import os
import json

def criar_arquivo_json_vazio(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            # Cria o arquivo com um objeto JSON vazio
            json.dump({}, f, indent=4)
        print(f"Arquivo '{arquivo}' criado com um JSON vazio.")
    else:
        print(f"Arquivo '{arquivo}' já existe.")

def adicionar_dados_ao_json(arquivo, chave, valor):
    # Lê o conteúdo existente do arquivo JSON (se houver)
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            try:
                dados = json.load(f)  # Carrega os dados existentes no JSON
            except json.JSONDecodeError:
                dados = {}  # Se o arquivo estiver vazio ou corrompido, inicializa como um dicionário vazio
    else:
        dados = {}

    # Adiciona novos dados ao dicionário
    dados[chave] = valor

    # Escreve os dados atualizados de volta ao arquivo
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
    print(f"Dados adicionados: {chave}: {valor}")

# Exemplo de uso
outro_arquivo = 'example.json'
adicionar_dados_ao_json(outro_arquivo, 'guilherme', 'programador')