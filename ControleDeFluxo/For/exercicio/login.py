#criar um sistema que o usuario vai criar login e senhar e depois vai entrar

print("Cadastro Usuario")
email = str(input("Digite seu Email: ").upper())
senhar = int(input("Digite sua Senhar: ").strip())
tentativas = 3



for limite in range(tentativas):
        inserirLogin = str(input("Inserir Seu Email: ").upper())
        inserirSenhar = int(input("Informe Sua Senhar: "))
        if inserirLogin == email and inserirSenhar == senhar:
            print("Usuario Logado no Sistema")
            break
        else:
            print("Senhar ou loguin Invalido")
            tentativas -= 1
            print(f'Quantidade de tentativas Restantes {tentativas}')
            if tentativas == 0:
                 print("Usuario Bloqueado")
            