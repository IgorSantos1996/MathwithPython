# Importa operação Limit (limite) da biblioteca sympy
# Importa Symbol - possibilidade de operações com símbolos
# Importa função sympy S que transforma texto em algumas constantes padrão
# limite 1 / x com x tendendo a 3.
#


from sympy import Limit, Symbol, S

# Define uma função


def calcula_f(x):
    return 1 / x


# Define x como uma varável
x = Symbol('x')

# Calcula limite da função quando x -> 3
resultado = Limit(calcula_f(x), x, 3).doit()

print('Limite da função calcula_f para x -> 3')
print(resultado)
