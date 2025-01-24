velocidade = int(input("Inserir sua velocidade: "))

if velocidade > 110:
    print('Acima da Velocidade Permitida')
    print("Reduzir sua Velocidade")

elif velocidade <= 60:
    print("Favor Dirigir acima de 80Km")
else:
    print("Velocidade Permitida")    

