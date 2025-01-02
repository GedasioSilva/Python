def calculadora():
        print("Bem-vindo á calculadora Simples!")
        print("Escolha uma operação")
        print("1 Soma")
        print("2 Subtração")
        print("3 Multiplicação")
        print("4 Divisão")
        
        escolha = input("Digite a operação escolhida: (1-2-3-4): " )
        
        if(escolha in ['1','2','3','4']):
            number1 = float(input("Digite o Primeiro Número: "))
            number2 = float(input("Digite o Segundo Número: "))

            if escolha == '1':
                resultado = number1 + number2
                print("O Resultado da soma foi: {:.1f}".format(resultado))
            
            elif escolha == '2':
                resultado = number1 - number2
                print(f"O Resultado da subtração foi: {resultado}")
                
            elif escolha == '3':
                resultado = number1 * number2
                print("O Resultado da Multiplicação  foi {:.2f}".format(resultado))
                
            elif escolha == '4':
                if number2 != 0:
                    resultado = number1 / number2
                    print("O Resultado é {:.2f}".format(resultado))
                else:
                    print("Divisão por 0 Não é Permitida")            
        else:
            print("Escolha Invalida. Por favor , tente Novamente")


calculadora()
#print("O valor é {:.1f}".format(resultado))        