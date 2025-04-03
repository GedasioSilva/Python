#crie uma def que recebe o salario e outra que recebe
#o valor do aumento

def salario(salario_passado):#passando o valor
    salario_minimo = salario_passado
   
    def aumento(valor_aumento=''):
        nonlocal salario_minimo
        salario_minimo = salario_minimo / 100 * valor_aumento
        return salario_minimo #retorna o salario minimo
    return aumento #retorna o aumento   


novo_salario = salario(1500)
print(novo_salario(10))


print(15*'--','SEPARANDO CONTEUDO')