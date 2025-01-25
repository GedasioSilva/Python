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
    

condicao = True

while condicao:
    nome = input('Qual é o seu Nome: ')
    print(f'Seu nome é: {nome}')
    print(f"Ou Digite sair pra Acabar")

    if nome == 'sair':
        break
print('Acabou')    