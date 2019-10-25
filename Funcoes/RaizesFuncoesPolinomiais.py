# Importa função de calculo de raiz (roots) da biblioteca numpy
#

from numpy import roots

print("\n"*100)
# Define coeficientes da função do primeiro grau 2x + 1
coeficientes = [2, 1]
raiz = roots(coeficientes)

print("\n")
print("Raiz da função 2x + 1")
print(raiz)

# Define coeficientes da função do segundo grau x **2 - 4x + 3
coeficientes = [1,-4, 3]
raiz = roots(coeficientes)
print("\n")
print("Raizes da função x**2 - 4x + 3")
print(raiz)

# Define coeficientes da função do segundo grau x**2 - 4x + 3
coeficientes = [1, -4, 3]
raiz = roots(coeficientes)

print("\n")
print("Raizes da função x**2 + x + 1")
coeficientes = [1, 1, 1]
raiz = roots(coeficientes)
print("\n")
print("Raizes da função x**2 + x + 1")
print(raiz)

# Define coeficientes da função do terceiro grau 3x**3 - 11x**2 + 5x + 3
coeficientes = [3, -11, 5, 3]
raiz = roots(coeficientes)
print("\n")
print("Raizes da função 3x**3 - 11x**2 + 5x + 3")
print(raiz)
