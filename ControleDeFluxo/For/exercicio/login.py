#criar um sistema que o usuario vai criar login e senhar e depois vai entrar

print("Cadastro Usuario")
email = str(input("Digite seu Email: ").upper())
senhar = int(input("Digite sua Senhar: ").strip())
celular = int(input("Informe seu Número de celular: ").strip())

for limite in range(3):
        tentativas = 2 #tentativas dando error
        inserirLogin = str(input("Inserir Seu Email: ").upper())
        inserirSenhar = int(input("Informe Sua Senhar: "))
        if inserirLogin == email and inserirSenhar == senhar:
            print("Usuario Logado no Sistema")
            break
        else:
            print("Senhar ou loguin Invalido")
            tentativas = tentativas - 1 
            print(f'Quantidade de tentativas Restantes {tentativas}')
            




print(" ")
print("úsuario Bloqueado")

print("Opção 1 Verificação Pelo Email: ")
print("Opção 2 Verificação Pelo Celular: ")
escolhar = input("Digite a Opção Escolhida: ")

def recuperacao(escolhar):
    if int(escolhar) == 1:
            print("Email pra alterar senhar Enviado")     
    elif int(escolhar) == 2:
            print("SmS Enviado pro seu Número:")
    else:
          print("Opção Escolhida foi Invalida: ")
recuperacao(escolhar)