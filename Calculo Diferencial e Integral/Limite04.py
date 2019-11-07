# Importa operação Limit (limite) da biblioteca sympy
# Importa Symbol - possibilidade de operações com símbolos
# Importa função sympy S que transforma texto em algumas constantes padrão
# limite sin 2x / x com x -> pi/6
#


from sympy import Limit, Symbol, S, sin
from math import pi

# Define uma função


def calcula_f(x):
    return sin(2*x) / x


x = Symbol('x')
resultado = Limit(calcula_f(x), x, pi/6).doit()
print(resultado)
