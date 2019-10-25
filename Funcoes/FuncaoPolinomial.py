# Define uma nova função. Neste caso, uma função polinomial
#
def calcula_f(x):
    return 3 * x**3 - 4 * x**2 + 2 * x - 5

print("\n" * 100)

# Chama a função para calcular o valor para x = 3.0
x = 3.0
y = calcula_f(x)

print("\n")
print("Resultado da função calcula_f para x = 3.0")
print("y = ", y)