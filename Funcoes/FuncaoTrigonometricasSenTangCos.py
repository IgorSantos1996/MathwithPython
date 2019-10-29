# Importa a função trigonométrica sin (Seno) da biblioteca
# Importa também a constante pi
#
from math import sin, pi, cos, tan
# Define uma nova função. Neste caso, uma função trigonométrica


def calcula_f(x):
    return 2 * sin(x / 4 + pi / 8) + (1.0 / 4) * cos(2 * x - pi) - (1.0 / 3) * tan(x + pi)


print("\n" * 100)

# Usa função calcula_f. Argumento em radianos
y = calcula_f(pi / 4)
print("\n")
print("Resultado da função calcula_f para argumento pi / 4")
print("y = ", y)

# Usa função calcula_f. Argumento em radianos
y = calcula_f(3 * pi / 4)

print("\n")
print("Resultado da função calcula_f para argumento 3 * pi /4 ")
print("y", y)
