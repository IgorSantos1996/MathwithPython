# Define uma nova funçao. Neste casoo,uma funcao exponencial
#


def calcula_f(a, x):
    return 3 * a**(x/a)


# Limpa a area de console para facilitar a visualização do resultado
print("\n" * 100)

# Chama a função para calcular o valor quando a = 2 e x = 4.0
a = 2
x = 4.0
y = calcula_f(a, x)

print("Resultado da funcao calcula_f de base a = 2 e x = 4")
print("y = ", y)

# Chama a funcao para calcular o valor quando a = 3 e x = 3.0
a = 3
x = 3.0
y = calcula_f(a, x)

print("\nResultado da funcao calcula_f da base a = 3 e x = 3.0")
print("y = ", y)
