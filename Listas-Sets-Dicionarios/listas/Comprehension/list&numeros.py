valores = []

for x in range(6):
    valores.append(x * 10)
    
print(valores)


#dentro de uma list comprehension
#vai fazer o x vezes 10 dentro do for rodando 6 vezes 
valores2 = [x * 10 for x in range(6)]
print(valores2)
    