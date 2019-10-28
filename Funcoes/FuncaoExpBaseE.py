# Importa funcao exp (exponencial) da biblioteca math
#
from math import exp

# Define uma nova funcao. Neste caso, uma funcao exponencial


def calcula_f(x):
    return 2 * exp(3 * x)


print("\n" * 100)

# Chama a funcaopara calcular o valor para x = 3.0
x = 3.0
y = calcula_f(x)
print("\n")
print("Resultado da funcao calcula_f para x = 3.0")

print("y = ", y)

# Chama a funcao para calcular o valor para x = 1.0/2
# Neste caso, para que a operaçao seja feita com ponto flutuante,
# numerador ou denominador (ou ambos) deve ser escrito usando sua casa decimal
x = 1.0 / 2
y = calcula_f(x)

print("\n")
print("Resultado da funcao calcula_f para x = 1.0 / 2")
print("y = ", y)
