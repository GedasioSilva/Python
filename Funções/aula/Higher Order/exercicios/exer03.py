#exercitando funções de primeira classes

#essa função é feita pra calcular o valor
def dezporcento(valor):
    dez = 10 * valor / 100
    return f'o seu salario é {valor } o seu aumento foi de :R${dez:.2f}'

def vinteporcento(valor):
    vinte = 20 * valor /100
    return f'o seu salario é {valor } o seu aumento foi de :R${vinte:.2f}'

#essa função é feita pra receber a função de calculo e o salario
def calculodeaumento(funcao,salario):
    return funcao(salario)

#aqui fazemos o calculo da função aumento 
aumentodedez = calculodeaumento(dezporcento,1500)
print(aumentodedez)

#pegando a função do valor de 20 porcento
aumentodevinte = calculodeaumento(vinteporcento,1500)
print(aumentodevinte)