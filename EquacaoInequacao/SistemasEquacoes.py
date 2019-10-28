# Importa Symbol - possibilidade de operacoes com simbolos
# Importa Solve - permite solucao de equacoes
from sympy import Symbol, solve

# Define duas novas


def calcula_f1(x, y):
    return -2*x + 4*y - 5


def calcula_f2(x, y):
    return 3*x - 2*y-3


print("\n" * 100)
# Define x e y com variaveis
x = Symbol('x')
y = Symbol('y')

# Resolve o sistema de equacoes
g = calcula_f1(x, y)
h = calcula_f2(x, y)

resultado = solve((g, h))

print("\n")
print("Resultado do sistema de equacoes")
print(resultado)
