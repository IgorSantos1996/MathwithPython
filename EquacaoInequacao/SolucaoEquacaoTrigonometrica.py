# Importa Symbol - possibilidade de operacoes com simbolos
# Importa solve - permite solucao de equacoes
# Importa funcoes seno(sin), cosseno(cos), tangente(tan)

from sympy import Symbol, solve, sin, cos, tan

# Define uma nova funcao


def calcula_f(x):
    return (sin(2 * x))**2 - cos(2 * x) - tan(2*x) - 1


print("\n" * 100)

# Define x como uma variavel
x = Symbol('x')

# Resolve a equacao calcula_f = 0
y = calcula_f(x)

resultado = solve(y)
print("\n")
print("Resultado da equacao (sin(2*x))**2 - cos(2 * x) - tan(2*x) - 1 = 0")
print("x = ", resultado)
