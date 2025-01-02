#criar um programa que calcula a quantidade de tinta
#necessaria para pintar um parede . o usuario devera fornecer as seguintes
#informações rendimento , altura e largura
#o programa deve mostrar na tela a mensagem voce necessicta de x latas de tintas

redimento = float(input("Informe o Rendimento da Lata: "))
largura = float(input("Qual é a largura da parede: "))
altura = float(input("Qual é a Altura da parede: "))

def area(rendimento,largura,altura):
    areaTotal = largura * altura
    resultado = areaTotal / rendimento
    print(f'Para pintar {areaTotal} precisa de {resultado:.2f} latas de tintas')
     

area(redimento,largura,altura)