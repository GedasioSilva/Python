#fazer um programa pra verificar os pontos das carnes
#verificando tela temperatura em que estado a carne está
#48*c Selada
#54*C AO Ponto Para mal
#60*C Ao Ponto
#65*C Ao ponto para o bem
#71*C bem passada  

pontoCarne = int(input("Informe o a temperatura da Carne: "))

if pontoCarne < 48:
        print("Cozinha por mais alguns minuntos")
        
elif pontoCarne in range(48,53):
    print("Selada!")
elif pontoCarne in range(54,59):
    print("AO Ponto Para mal!")
elif pontoCarne in range(60,64):
    print("ao ponto!")
elif pontoCarne in range(65,70):
    print("Ao ponto para bem Passada!")        
elif pontoCarne >= 71:
    print("Carne bem Passada!")
