# Importa operação Limit (limite) da biblioteca sympy
# Importa Symbol - possibilidade de operações com símbolos
# Importa função sympy S que transforma texto em algumas constantes padrão
# limite x^3 -1 / x-1 com x tendendo a 1.
#


from sympy import Limit, Symbol, S

# Define uma função


def calcula_f(x):
    return (x**3 - 1) / (x-1)


x = Symbol('x')
resultado = Limit(calcula_f(x), x, 1).doit()

print(resultado)
