 #usamos o all quando importamos import conteudo from *
#dessa forma eu mostro quando pedir 
# apenas oque eu vou deixar pegar nesse arquivo
__all__ = [
    'bemvindo',
    'adeus'
]
variavel = "Conteudo que esta dentro da pasta conteudo"


def bemvindo():
    return 'Seja bem vindo'

def adeus():
    return 'Até a Proxíma'