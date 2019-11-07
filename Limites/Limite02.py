# Importa operação Limit (limite) da biblioteca sympy
# Importa Symbol - possibilidade de operações com símbolos
# Importa função sympy S que transforma texto em algumas constantes padrão
# limite 1 / x com x tendendo a - infinito.
#


from sympy import Limit, Symbol, S

# Define uma função


def calcula_f(x):
    return 1 / x
x = Symbol('x')


# Calcula limite da função quando x -> + infinito
resultado = Limit(calcula_f(x), x, -S.Infinity).doit()
print(resultado)
