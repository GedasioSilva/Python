#crie uma função onde recebe dois valores senhar e lguin faça a validação
#verificando se a senhar tem 6 digitos e se é int
#verifique se o nome é string e se os termos foram concordados

def verifica(nome,senhar,termo):
    condicoes = 0
    if isinstance(nome,str) and len(nome) >= 6 :
            print("Loguin é valido")
            condicoes += 1            
    else:
        print("loguin invalido")


    if isinstance(senhar,int) and senhar > 6:
        print(f"Sua senhar é valida")
        condicoes += 1     
    else:
        print("senhar invalida")
        

    if isinstance(termo,bool):
        print("O Termo foi aceito")
        condicoes += 1  
    else:
         print("O termo não foi aceito")

  
    resultado = "Cadastro Aprovado" if condicoes >= 2  else "cadastro não aprovado" 
    return(resultado)


cadastro = verifica(nome='dasiio',senhar=12345,termo=False)
print(cadastro)                