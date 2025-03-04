#Try , except , finally Aula 174 caso duvidas futuras

try: #tenta executar o programa
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError: #error porque a divisão n pode ser por zero
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
