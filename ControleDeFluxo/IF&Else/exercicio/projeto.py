

renda_acima_5mil = float(input("Quanto você recebe por mês?  "))
nome_limpo = input("Seu nome esta Limpo: ")


if renda_acima_5mil >= 5000 and nome_limpo.upper() ==  "SIM":
    print("Financiamento Aprovado")
else:
    print("Financiamento Negado")    