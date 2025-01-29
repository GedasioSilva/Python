#vazer uma calculadora com while
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro Número: ')
    operador = input('Digite o Operador (+-/*): ')

    numeros_validos = None #flag numeros validos = none
    num_1_float = 0
    num_2_float = 0

    try: #tentando converter os números
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True #se forem convertidos o numeros validos = true
    except:
        numeros_validos = None #se der errado numeros_validos = none

    if numeros_validos is None: #aqui verifica se os numeros forem convertidos
        print('Um ou Ambos números digitados são invalidos.')
        continue
    
    operadores_permitidos = '+-/*' #os operadores permitidos

    if operador not in operadores_permitidos: #verifica se não tem os o operador informado
        print('operador Inválido')
        continue

    if len(operador) > 1: #verifica se foi informado mais de um operador
        print('Digite apenas um operador')
        continue

    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'O Resultado de {num_1_float} + {num_2_float} é:{resultado:.2f}')

    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'O Resultado de {num_1_float} - {num_2_float} é: {resultado:.2f}')
    
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'O Resultado de {num_1_float} * {num_2_float} é {resultado}')

    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'O resultado de {num_1_float} / {num_2_float} é {resultado}')

    sair = input('Quer sair [s]im:').lower().startswith('s') #verifica se a primeira letra é s
    if sair is True:
        break