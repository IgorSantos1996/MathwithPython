# Importa funcoes exp (exponencial) e sin (seno) da biblioteca math

from math import exp, sin


def calcula_f(x):
    return 2 * exp(x / 2) - 3 * sin(x) + 2 * x**3 - 5


print("\n" * 100)

# Chama a funcao para calcular o valor para x = 3.0
x = 3.0
y = calcula_f(x)

print("\n")
print("Resultado da funcao calcula_f para x = 3.0")
print("y = ", y)
