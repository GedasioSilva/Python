#Exercicio - Criar sistema de perguntas e respostas 
perguntas = {
    "primeira":{
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    "segunda" : {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    "terceira" : {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
}

contadorAcertos = 0
contadorErros = 0
print("Pergunta: Quanto é 5 + 5 ?")
print("Opções")
print("0) 25")
print("1) 55")
print("2) 10")
print("0) 51")

resposta = int(input("Informe sua Resposta: "))
print(resposta)
if resposta == perguntas["primeira"]["Resposta"]:
    print("Acertou")
    contadorAcertos += 1
else:
    print("Errow")
    contadorErros += 1  

print("Pergunta: Quanto é 5 * 5 ?")
print("Opções")
print("0) 25")
print("1) 55")
print("2) 10")
print("3) 51")
resposta = int(input("Informe sua Resposta: "))
print(resposta)
if resposta == perguntas["segunda"]["Resposta"]:
    print("Acertou")
    contadorAcertos += 1
else:
    print("Errow")
    contadorErros += 1  