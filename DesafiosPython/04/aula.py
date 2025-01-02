#calculadora IMC 

#menor que 18,5 Magreza
#entre 18.5 e 24.9 Normal
#Entre 25.0 e 29.9 SobrePeso
#entre 30.0 e 39.9 Obesidade
#maior que 40.0 Obesidade Grave


altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu Peso: "))

imc = peso /altura**2
print(f'Seu valor do imc {imc:.2f}')


if imc < 18.5:
    print("Magro")
elif imc > 18.5 and imc < 24.9:
    print("Normal")
elif imc > 25 and imc < 29.9:
    print("Sobre Peso")
elif imc > 30 and imc < 39.9:
    print("Obsidade")
elif imc >= 40:
    print("Obesidade Grave")   
             