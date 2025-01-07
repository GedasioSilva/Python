#pegar 2 valores e fazer as 4 operações
#usando a formatação de string para usar as casa decimais

primeiro = float(input("Informe o primeiro valor: "))
segundo = float(input("Informe o segundo valor: "))


def somar(primeiro,segundo):
    resultado = primeiro + segundo
    return (f'A soma deu {resultado:.2f}')

print(somar(primeiro,segundo))

def subitrair(primeiro,segundo):
    resultado = primeiro - segundo
    return(f'A subtração deu {resultado:.2f}')

print(subitrair(primeiro,segundo))

def multiplicar(primeiro,segundo):
    resultado = primeiro * segundo
    return(f'A multiplicação De {resultado:.2f}')

print(multiplicar(primeiro,segundo))

def divisao(primeiro,segundo):
    resultado = primeiro / segundo
    return(f'A divisão deu {resultado:.2f}')

print(divisao(primeiro,segundo))

#multiplica o primeiro por segundo vezes 
def exponenciacao(primeiro,segundo):
    resultado = primeiro ** segundo
    return(f'O Resultado da exponenciação deu {resultado:.2f}')

print(exponenciacao(primeiro,segundo))
