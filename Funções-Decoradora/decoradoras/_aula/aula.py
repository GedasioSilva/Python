# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar sintático)
#aula 190

def criar_funcao(func): # recebe a função
    def interna(*args, **kwargs): #recebe argumentos
        print('Vou te decorar')
        for arg in args: #verifica cada args
            e_string(arg) #passa cada dado pra outra string
        resultado = func(*args, **kwargs) #resultado da func
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado #mosta o resultado
    return interna

def inverte_string(string): #inverte as string
    return string[::-1]

def e_string(param): #recebe oque foi passado da interna e verifica se é string
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
inverte_string_checando_parametro = criar_funcao(inverte_string) #varivavel que recbe a função que recebe outra função
invertida = inverte_string_checando_parametro('123')
print(invertida)