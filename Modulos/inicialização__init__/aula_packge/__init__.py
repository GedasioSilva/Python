#é um arquivo logo quando packge é instanciado
#vc importa o pacote ai esse código já vai ser executado
print('Você importou o packge', __name__)
from aula_packge.modulo import bemvindo
 
def dobra(x):
    return x * 2

print(bemvindo)

