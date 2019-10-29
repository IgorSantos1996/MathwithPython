# Importa Symbol - possibilidade de operações com símbolos
# Importa solve - permite solução de equações
#
from sympy import Symbol, solve
# Define duas novas funcoes


def calcula_f1(x, y, z):
    return -2 * x + 4 * y - z - 5


def calcula_f2(x, y, z):
    return 3 * x - 2 * y + 4 * z - 3


def calcula_f3(x, y, z):
    return -x + 5 * y - 4 * z - 3


# Limpa a area de console para facilitar a visualização do
print("\n" * 100)

# Define x, y, z como variaveis
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# Resolve o sistema de equacoes
f = calcula_f1(x, y, z)
g = calcula_f2(x, y, z)
h = calcula_f3(x, y, z)

resultado = solve((f, g, h))
print('\n')
print("Resultado do sistema de equacoes: ", resultado)
