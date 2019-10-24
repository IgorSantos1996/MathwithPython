# Importa biblioteca numpy que permite trabalhar com matrizes
# Função matrix para definir matrizes
# Função multiply para multiplicação de elemento por elemento
#
from numpy import matrix,  multiply

print("\n" * 100)

# Cria matriz A com valores inteiros (int)
matriz_A = matrix([
    [7, 2, 4],
    [3, 5 ,9]
])
print("Matriz A")
print(matriz_A)

matriz_B = matrix([
    [3, 6, 9],
    [1, 8, 2]
])
print("\n")
print("Matriz B")
print(matriz_B)

# Multiplicação, elemento por elemento, da matriz A pelo B
resultado = multiply(matriz_A, matriz_B)
print("\n")
print("Multiplicação, elemento por elemento, da Matriz A pelo B. ")
print(resultado)