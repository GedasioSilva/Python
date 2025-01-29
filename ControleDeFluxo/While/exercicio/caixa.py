#Programa pra simular um caixa eletronico

saldo = 0
while True:
    print("1: consultar saldo\n")
    print("2: Depositar\n")
    print("3: sacar dinheiro\n")
    print("4: Sair")

    opcao = input("Escolhar uma opcao: ")

    if opcao != '1234':
        print("Opção informada invalida")

    if opcao == '1':
        print(f'Seu saldo é {saldo}')

    elif opcao == '2':
        deposito = float(input("Valor do deposito: "))
        saldo = deposito

    elif opcao == '3':
        sacar = float(input("Valor do saque"))

        if sacar > saldo:
            print("Valor do saque é invalido")
        else:
            print(f'Saque valido: {sacar}') 
              
    if opcao == '4':
        break
