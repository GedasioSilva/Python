def pontencia(base,expoente=2):
    return base ** expoente

user_base = int(input("Digite o número Base: "))
user_expoente = input("Digite o número expoente o expoente padrão é 2 :  ")

if user_expoente:
    print(f'O resultado é: {pontencia(user_base,user_expoente)}')