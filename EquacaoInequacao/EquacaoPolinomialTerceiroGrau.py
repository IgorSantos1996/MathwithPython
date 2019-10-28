from sympy import Symbol, solve

# Define uma nova funcao


def calcula_f(x):
    return 3 * x**3 - 11 * x**2 + 5 * x + 3


print("\n" * 100)

# Define x como uma variavel
x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)

print("\n")
print("Resultado da equacao 3 * x**3 -11 * x**2 + 5 * x + 3")
print("x = ", resultado)
