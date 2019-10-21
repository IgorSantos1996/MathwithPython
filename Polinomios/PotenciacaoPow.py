# Importa função pow (potencia) da biblioteca math
#
from math import pow

# Define valores
a = 2
b = 6
# Operações com potências
a_quadrado = pow(a, 2)
a_cubo = pow(a, 3)
a_quarta = pow(a, 4)
a_elevado_b = pow(a, b)
print("Resultado das operações ")
print(f"(a) elevado a 2 = {a_quadrado}")
print(f"(a) elevado a 3 = {a_cubo}")
print(f"(a) elevado a 4 = {a_quarta}")
print(f"(a) elevado a (b)  = {a_elevado_b}")
