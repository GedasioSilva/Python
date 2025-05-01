import json
caminho = 'C:\\PYTHON\\Python\\Json\\execicios\\' #pegando o caminho
caminho += 'exer01.json' #se não tiver criar

dados = { #criando os dados que vai pra dentro do json
    "nome":"gedasio",
    "sobrenome":"silva",
    "data_nasc":1995
}

with open(caminho ,'w+',encoding='utf8') as arquivo:
    json.dump(
        dados, #onde os arquivos estão
        arquivo, # o caminho
        ensure_ascii=False, #acentuação
        indent=2, #indentação
              )
    arquivo.seek(0,0)
    dados['nome'] = 'Camila' #alterando o valor dentro do json
    print(dados['nome'])
    print(arquivo.read())




