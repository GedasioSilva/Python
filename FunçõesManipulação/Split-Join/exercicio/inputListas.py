#criar uma lista onde recebe os dados passados pelo Usuario

frutas_usuario = input(" Digitar a lista de frutas separado por virgula: ")

frutas_lista = frutas_usuario.split(',') #separando por virgula e tirando o espaço

#verificando se o usuario informou alguma fruta escolhida
#pegando os dados passados pelo input e crio uma lista e depois 
#procuro se sua lista tem a escolhida
fruta_escolhida = 'goiaba'
fruta = 0

while fruta < len(frutas_lista):
    if fruta_escolhida == frutas_lista[fruta]:
        print(fruta)
        print(f"Achei a sua fruta ela é a : {frutas_lista[fruta]}")
        break
    else:
        print(f'Sua fruta é ? {frutas_lista[fruta]}')
        fruta += 1

