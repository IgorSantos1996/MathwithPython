# Importa Symbol - possibilidade de operacoes com simbolos
# Importa solve - permite solucao de equacoes

from sympy import Symbol, solve

# Define uma nova funcao

def calcula_f(X):
    return x ** 2 - 4 * x + 3


print("\n" * 100)

# Define x como uma variavel
x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)

print("\n")
print("Resultado da equacao x**2 - 4  + x + 3 = 0")
print("x = ", resultado)


