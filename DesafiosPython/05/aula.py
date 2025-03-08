#Estou pegando de Produtos oque ele tiver
import copy #vou importar im modulos de copia

from dados import produtos
#criando uma lista que copia o dicionario produtos
novos_produtos = [ #nova lista
    #desempacotando preco e depois arredondando e chamando o preco
    #depois coloca o preco * 1.1 , com 2 casas decimais
   {**p, 'preco':round(p['preco'] * 1.1 , 2)} 
   for p in  copy.deepcopy(produtos)
]

#ficar consultado ver se aumenta na lista produtos

print(*produtos,sep='\n')
print(" ")
print(*novos_produtos,sep='\n')

print(10*'-','SEPARANDO EM PARTES ', 10*'-')

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos_odenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome']
)

print(*produtos,sep='\n')
print(" ")
print(*produtos_odenados_por_nome,sep='\n')


print(10*'-','SEPARANDO EM PARTES ', 10*'-')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_odenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco']
)

print(*produtos,sep='\n')
print(" ")
print(*produtos_odenados_por_nome,sep='\n')