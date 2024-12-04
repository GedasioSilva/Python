compra_confirmada = True
dados_compra = 'Compra no valor de R$:12.50 e entrega confirmada'
limite = 3

for limite in range(3):
    compra_confirmada = (input("sua compra foi confirmada: ")).upper()
    if compra_confirmada == "SIM":
        print(dados_compra)
        print('Detalhes enviados para o seu Email')
        break
    else:
        print("Compra não Realizada")    