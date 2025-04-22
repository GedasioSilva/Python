from itertools import count

#estou pegando o valor e adicionando mais 1

c1 = count()
print(next(c1))
print(next(c1))

for i in c1:
    if i > 3:
        break
    print(i)