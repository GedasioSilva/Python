#json só aceita dados simples
import json
caminho_arquivo = 'C:\\PYTHON\\Python\\json\\'
caminho_arquivo += 'aula.json'

"""
#aqui crio o json e crio um arquivo pra guarda as informações
pessoa = {
    "nome": "Luiz Otávio 2",
    "sobrenome": "Miranda",
    "enderecos": [
        {"rua": "R1","numero": 32},
        {"rua": "R2","numero": 55}
    ],
    "altura": 1.8,
    "numeros_preferidos": [2,4,6,8,10],
    "dev": True,
    "nada": None
    }

#open #abrir o arquivo se não tiver cria , utf8 acentuações
with open(caminho_arquivo,'w',encoding='utf8') as arquivo:
    json.dump(pessoa,
              arquivo,
              ensure_ascii=False, #colocar com acentuação
              indent=2,
            ) #coloca indentado
"""
#json é uma forma de pegar os dados salvados no arquivo
with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])            