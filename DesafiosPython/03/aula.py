'''
lista1 = funcionarios que tem carro e trabalha a noite
lista2 = funcionarios que tem carro e trabalha durante o dia
lista3 = funcionarios que não tem caro 
'''
funcionarios = ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos','Alice','Bruno','Melissa']

#tem carro e trabalhar a noite
lista1 = set(tem_carro).intersection(turno_noite)
print(f'funcionario que tem carro e trabalhar a noite: {lista1}')

print(" ")
#tem carro e trabalha de dia
lista2 = set(tem_carro).intersection(turno_dia)
print(f'funcionarios que trabalham de dia e tem carro {lista2}')

print(" ")

#funcionario que não tem carros
lista3 = set(funcionarios).difference(tem_carro)
print(f'funcionarios que não tem carros {lista3}')