def pontencia(base,expoente=2): #função com valor padrão
    return base ** expoente

#as entradas de dados da base e expoente
user_base = int(input("Digite o número Base: "))
user_expoente = input("Digite o número expoente o expoente padrão é 2 :  ")

#verifica se foi usado o expoente sem validação só mostrando que foi usado
if user_expoente:
    print(f'O resultado é: {pontencia(user_base,user_expoente)}')
else: #aqui seria o contrario da primeira afirmação
    print(f'O Uso do Expoente default que tem o valor 2')
    print(f'O Resultado é {pontencia(user_base)}')    