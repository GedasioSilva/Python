#vou criar uma lista onde vou passando os index até achar um determinador valor

lista_nomes = ['gedasio','camila','núbia','diana','tino']
iterator = iter(lista_nomes)

#fica procurando até achar o nome diana
while True:
    print("Procurando")
    if next(iterator) == 'diana':
        print("Achei")
        break
    