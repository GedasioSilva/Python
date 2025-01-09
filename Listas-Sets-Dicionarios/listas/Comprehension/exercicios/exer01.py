#expressão simples 
#vai contar do index x ate o x que no caso recebe o range 5
numeros = [x for x in range(5)]
print(numeros)

#aplicar tranformações
#vai rodar de 0 ate 4 o primeiro index é 0 e o ultimo é 4
#0x0 da 0 depois 1 * 1 da 1 em diante
quadrados = [x ** 2 for x in range(5)]
print(quadrados)

#adicionar uma condição para incluir apenas elementos que atendem ao criterio
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

impares = [x for x in range(10) if x % 2 == 1]
print(impares)