#verifica se termos sua fruta e se não tiver continua perguntando
fruta = 'abacate'
escolhar = input("Informe a sua fruta: ").lower()

if fruta == escolhar:
        print('Temos sua fruta')
else:
    while fruta != escolhar:
        escolhar = input("Tente Informa outra Fruta: ")
        if fruta == escolhar:
             print("Obrigado Temos Sua Fruta")
    

    