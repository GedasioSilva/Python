#primeiro a saida se sim depois a condição depois a saida se não
x = 10
resultado = "Positivo" if x > 0 else "Negativo"
# ou reescrevendo:
resultado = (x > 0 and "Positivo") or "Negativo"
print(resultado)  # Saída: Positivo


#desbloquear contar

#entrada de dados 
resposta = str(input('Deseja desbloquear SIM OU NÃO: ').upper())
condicao = 'desbloqueado' if resposta == 'SIM' else "Bloqueado" 
print(condicao)

#verifica se o salario vai ser aumentado ou não
x1 = 1500
aumento = 'Salario aumentado' if x1 < 1500 else 'Salario Não aumentado'
print(aumento)

x2=0
result = 'Maior' if x2 > 1 else 'menor' 
print(result)