# Importa Symbol - possibilidade de operacoes com simbolos
# Importa solve - permite solucao de equacoes

from sympy import Symbol, solve

# Define uma nova funcao
def calcula_f(x):
    return 2 * x + 1

print("\n" * 100)

x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)
print("\n")
print("Resultado da equacao 2 * x + 1 = 0")
print("x = ", resultado)
