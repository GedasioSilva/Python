# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs): #a diferença é que a função fica protegida dentro de uma class
        print('Oi', args, kwargs)


def funcao(*args, **kwargs): #funão normal
    print('Oi', args, kwargs)


c1 = Classe()#chamando a função protegida
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)