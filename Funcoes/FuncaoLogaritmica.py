# Importa funcao logaritmica (log) da biblioteca math
#
from math import log

# Define uma nova funcao, Neste funcao. Neste caso, uma funcao logaritmica


def calcula_f(x, a):
    return 3 * log(x / 2, a)


# Limpa a area de console para facilitar a visualizacao do resultado
print("\n" * 100)

# Chama a funcao para calcular o valor para base a = 10 e x = 25
x = 25.0
a = 10
y = calcula_f(x, a)

print("\n")

print("Resultado da funcao calcula_f para base a = 10 e x = 25.0")
print("y = ", y)

# Chama a função para calcular o valor para base a = 3 e x = 2.5
x = 2.5
a = 3
y = calcula_f(x, a)

print("\n")
print("Resultado da funcao calcula_f para base a = 3 e x = 2.5")
print("y = ", y)
