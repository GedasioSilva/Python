#sistema de calculo do aumento salarial
salarioBase = "Salario Minino"
salarioClass1 = "Salario Gerente"
salarioClass2 = "Salario Superviso"

horasPorDia = int(input("Horas trabalhadas por Dia: "))
valorHora = float(input("Informe o valor da hora trabalhada: "))
diaspormes = 26

mediaSalario = (horasPorDia * valorHora) * diaspormes

if mediaSalario <= 1412:
    print(f'{mediaSalario} {salarioBase}')
elif mediaSalario >1413 and mediaSalario < 2500:
    print(f'{mediaSalario} {salarioClass1}')
elif mediaSalario > 2500 :    
    print(f' {mediaSalario} {salarioClass2}')


