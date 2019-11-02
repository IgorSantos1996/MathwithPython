# Importa biblioteca numpy que trabalhar com matrizes
# Função matrix para definir matrizes
# Função linalg para fazer matriz inversa
#
from numpy import matrix, linalg

print("\n" * 100)

# Cria matriz A com valores inteiros (int)
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])
print('Matriz A')

print(matriz_A)

# Cria matriz inversa de A
matriz_A_inv = linalg.inv(matriz_A)


print("\n")
print("Matriz inversa de A")
print(matriz_A_inv)
