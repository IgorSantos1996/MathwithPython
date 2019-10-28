# Importa Symbol - possibilidade de operações com simbolos
# Importa solve - permite soluçao de equacoes
# Importa funcao logaritmica (log)

from sympy import Symbol, solve, log
# Define uma nova funcao


def calcula_f(x):
    return log(3 * x + 2, 4) - log(2 * x + 5, 4)


print("\n" * 100)
# Define x com uma variavel
x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)

print("\n")
print("Resultado da equacao log(3 * x + 2,4) - log(2 * x + 5, 4) = 0")
print("x = ", resultado)
