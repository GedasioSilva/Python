#criando uma lista e verificado se a cidade esta na lista

cidades = ('pernambuco','rio de Janeiro','São Paulo')
cidadeEscolhida = 'Pernambuco'.lower()

if cidadeEscolhida in cidades:
    print(f'A Cidade {cidadeEscolhida} está na lista')
else:
    print('A cidade não Esta')    