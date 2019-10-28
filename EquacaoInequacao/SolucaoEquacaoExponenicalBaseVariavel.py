# Importa Symbol - possibilidade de operacoes com simbolos
# Importa Solve - permite solucao de equacoes

from sympy import Symbol, solve


def calcula_f(x):
    return x**(x**2 - 7 * x - 18) - 1


print("\n" * 100)

x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)
print("\n")
print("Resultado da equacao x**(x**2 - 7 * x -18) - 1 = 0")
print("x = ", resultado)
