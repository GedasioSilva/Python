#criar um valor aleatorio e validar se se ganhou um premio ou não

import random

aleatorio = random.randint(1, 10)
print(aleatorio)

if aleatorio == 5:
    print("você ganhou o Premio")
else:
    print("Não ganhou")    