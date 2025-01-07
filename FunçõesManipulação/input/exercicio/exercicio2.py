#sistema de calculo do aumento salarial
salarioBase = "Salario Minino"
salarioClass1 = "Salario De Gerente"
salarioClass2 = "Salario De Superviso"

horasPorDia = int(input("Horas trabalhadas por Dia: "))
valorHora = float(input("Informe o valor da hora trabalhada: "))
diaspormes = 26

mediaSalario = (horasPorDia * valorHora) * diaspormes

if mediaSalario <= 1412:
    print(f'seu salario é {mediaSalario:,.2f} seria {salarioBase}')
elif mediaSalario >1413 and mediaSalario < 2500:
    print(f'seu salarario é {mediaSalario:,.2f} seria {salarioClass1}')
elif mediaSalario > 2500 :    
    print(f'seu salario é {mediaSalario:,.2f} seria {salarioClass2}')


