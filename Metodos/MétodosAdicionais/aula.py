#keys(): Retorna as chaves do dicionário.

key = {"a":1,"b":2}
print(key.keys())

#values(): Retorna os valores do dicionário.
#os valores são 1 e 2 onde os objetos "a" e "b" recebem
print(key.values())

#items(): Retorna pares de chave-valor.
#retorna os pares de valores
print(key.items())

#get(): Retorna o valor de uma chave ou um valor padrão.
print(key.get("a", 0))
print(key.get("b", 0))

#update(): Atualiza o dicionário com pares chave-valor.
d = {"a":2}
d.update({"b":3})
print(d)