#criar uma função re recebe uma lista e valida os dados

def valida(valores):
        if valores > 10:
            print(f'é Maior que 10: {valores}')
        else:
            print(f'Não é maior que 10: {valores}')


valores = [10,8,9,11]
validar_dados = map(valida,valores)       
print(*list(validar_dados))

print("SEPARANDO O CONTEUDO")
print(" ")