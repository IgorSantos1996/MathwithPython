# Importa x da biblioteca sympy.bac para tratar da variavel
# Importa factor da biblioteca sympy para fatoração

from sympy.abc import x
from sympy import factor

resultado = factor(x**2 + 3 * x)
print("O resultado da fotaração do polinômio x**2 + 3 * x")
print(resultado)
print("\n")

resultado = factor(x**2 - 9)
print("\nResultado da fatoração do polinômio x**2 - 9")
print(resultado)

resultado = factor(x**2 - 4 * x + 4)
print("\nResultado da fatoração do polinômio x**2 - 4*x + 4")
print(resultado)

resultado = factor(x**2 +x - 6)
print("\nResultado da fatoração do polinômio x**2 +x - 6")
print(resultado)

resultado = factor(x**3 - 3*x**2 - 10*x + 24)
print("\nResultado da fatoração do polinômio x**3 - 3*x**2 - 10*x + 24")
print(resultado)

resultado = factor(x**3 - 3*x**2 - 10*x)
print("\nResultado da fatoração do polinômio x**3 - 3*x**2 - 10*x")
print(resultado)