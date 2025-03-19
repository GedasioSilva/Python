#desempacotamento em chamadas 
#de métodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tuple = 'python','é','legal'

#desempacotamento em chamadas de funções
#oque eu quero fazer é mostrar todos os itens em apenas uma linha
for nome in lista:
    print(nome,end= '') #dessa forma desempacoto em apenas uma linha

print(" ")
print(*lista) #mostrando toda a lista em uma linha
print(*tuple) #mostrando toda a tuple em apenas uma linha

salas = [
    ['Maria','Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda',(0,10,20,30,40)]
]
#se precisar olhar oque tem na lista chamamos 
# dessa forma pós  fica melhor de ver
print(*salas, sep='\n')