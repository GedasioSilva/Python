carros = {'fiat':'palio','vw':'gol','chevolet':'opala'}

escolher = str(input("Informe fabriacante e nome do carro ")).split()
for carro in carros:
    if carros[carro] == escolher[1]:
            print(f"O carro {escolher[1]} está Disponivel ")
            break
    else:
          print("Não temos o carro")
        

        