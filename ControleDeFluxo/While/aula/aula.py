#criar uma promoção do produto de 100 reais 
#depois ir baixando o valor do produto

valor = 100
dia = 1
#ver se o valor é maior que 20 depois imprime o valor depois tira 5 do valor

while valor > 20:
    print(f'O dia é: {dia} o produto vai ser vendido por: R$:{valor}')
    dia += 1
    valor -=5 
    