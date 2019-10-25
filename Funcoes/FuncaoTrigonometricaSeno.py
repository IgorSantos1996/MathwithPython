# Importa a função trigonométrica sin (Seno) da biblioteca
# Importa também a constante pi
#
from math import sin, pi
# Define uma nova função. Neste caso, uma função senoidal


def calcula_f(x):
    return 2 * sin(x/4)


print("\n" * 100)

# Usa a função calcula_f. Argumento em radianos
y = calcula_f(pi/2)

print("\n")
print("Resulstado da função calcula_f para argumento pi /2 ")
print("y = ", y)

# Usa função calcula_f. Argumento em radianos
y = calcula_f(3 * pi)

print("\n")
print("Resultado da função calcula_f para argumento 3 * pi")
print("y = ", y)
