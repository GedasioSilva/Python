cpf = '37696055003' 
#essa variavel nove_digitos ta pegando string
nove_digitos = cpf[:9] #pegando os index de 0 até 8
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
