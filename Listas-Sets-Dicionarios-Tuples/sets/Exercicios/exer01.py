
nomes1 = {"nubia","diana","camila","patino"}
nomes2 = {"diana","gedasio","patino","albus"}

#os nomes que tem apenas em 1 lista
resultado = nomes1.difference(nomes2) #diferença
resultado2 = nomes1.union(nomes2) #união
resultado3 = nomes1.intersection(nomes2) #tem em ambos

print(resultado)
print(resultado2)
print(resultado3)



numeros = {1,2,3,4,5}
numeros2 = {6,7,8}

print(numeros ^ numeros2)