# args e kwargs
# args - se refe a argumentos não nomeados
# kwargs - se refere aos keyword arguments (argumentos nomeados)

#recefere assim se eu criar um kwargs quando eu manda valores
#exemplo nome = 'joana' idade = 23 , vão cair tudo dentro do kwargs
def mostro_argumentos_nomeados(**kwargs):
    print(kwargs)


mostro_argumentos_nomeados(nome='Joana', idade = 21 , sexo = 'feminino')
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)