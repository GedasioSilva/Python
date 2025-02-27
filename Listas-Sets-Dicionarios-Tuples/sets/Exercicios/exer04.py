#diciona números e remove números
numeros = {1,2,3,4,5,6}
numeros.add(7)
numeros.remove(4)

if 4 in numeros:
    print("Esta na set Números")
else:
    print("Não esta em Números")

#exercicio 2 ir removendo os números que o Úsuarios pra 

numeropassado = [1,2,3,4,5]

numerosescolhidos = {1,2,3,4,5,6,7,8,9,10}

   
for remove in numeropassado:
    numerosescolhidos.remove(remove)
    print(f'Removeu o  {remove}')

if len(numerosescolhidos) == 5:
    print("Os números escolhidos foram removidos")
    for numero3 in numerosescolhidos:
      print(f'Os números que sobraram: {numero3}')
else:
    print("Os números escolhidos não foram removidos")      
 