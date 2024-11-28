#cadastro de dados

nomeCompleto = str(input("Nome e emal ")).split()

cpfconsulta = int(input("Informe seu Cpf"))
senhacadastrada = 123

if cpfconsulta == 12317566409:
    print("conta cadastrada no banco de dados")
    senhar = int(input("infome a senhar:"))
    if senhar == senhacadastrada:
        print("conta acessada")
    else:
        print("Error na senhar")
        input("informe email pra redefinir senhar ")    
        emailRedefinirsenhar = input




primeiroNome = str(nomeCompleto[0]).upper()
segundoNome = str(nomeCompleto[1]).upper()       
print(f'Primeiro nome {primeiroNome} segundo {segundoNome}')
