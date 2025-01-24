#seu nome 
#seu nome invertido
#seu nome contem espaços
#quantas letras tem seu nome
#primeira letra
#ultima letra
#vefica se os dados foram passado
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é:{nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print("Seu nome contem Espaços")
    else:
        print("Seu nome não contem espaços")

    print(f'Seu nome tem {len(nome)} caracteres')    
    print(f'Primeira letra do seu nome é {nome[0]}')
    print(f'última letra do seu nome é {nome[-1]}')
else:
    print("Dados invalidos")    
    

