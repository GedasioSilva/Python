produtoMaior = 30
produtoMenor = 10

if produtoMaior >= 20:
    comecao = produtoMaior / 5
    novovalor = produtoMaior - comecao
    print(f'valor da comição {comecao} valor do Produto {produtoMaior}')
    print(f'o valor do produto menos a comição : {novovalor} ')
else:
    print(f'produto menor que 20')    
    
print("--------------------------------------------------------")

valor = int(input("Digite o valor do seu produto: "))

if valor > 20:
    comicao = valor / 5
    print(f'o valor da comição: {comicao}')
else:
    print("o produto é menor que 20 Reais")        
    
print("--------------------------------------------------------")

valor1 = int(input('Informe o valor do produto: '))

while valor1 > 20:
        valor1 = (valor1 * 0.10) + valor1 
        print(f'o valor final do seu produto será de R$:{valor1}')
        break   