from datetime import datetime
#tem que fazer o import da biblioteca datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("em que ano vc nasceu: "))
calculo = (ano_atual - ano_nascimento)

print('sua Idade é: ' +  str(calculo))


