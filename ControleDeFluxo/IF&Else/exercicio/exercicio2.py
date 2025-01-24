#se o valor for maior que 20 e menor que 40
valor = 21

if valor >= 20 and valor <= 40:
    print("Produto foi aceito")
else:
    print("Não foi aceito")


#criando um input e verifica oque o usuario escreveu e desenvolver aparatir dai
entrada = str(input("Entrar ou Sair: ")).lower()

if entrada == "entrar": #verifica se foi informado entrar
    print("Entrada permitida")
elif entrada == "sair": #verifica se foi informado sair
    print("Saida Permitida")
else:#se não for nenhum dos dois 
    invalido = False #invalido recebe true
    while invalido == False: #enquanto invalido = true
        entrada = str(input("Valor de dados não identificado tentar novamente: ")).lower() #pede pra continuar informando
        if entrada == "entrar":
            invalido = True
            print("Dado informado Valido Obrigado")
        elif entrada == "sair":
            invalido = True
            print("Dado de saida Informado")
            


    
        