# Importa biblioteca numpy que permite trabalhar com matrizes
# Funcão matrix para definir matrizes
# Funcao power para fazer a potencia dos elementos da matriz
#
from numpy import matrix, power

# Limpa a area do console para facilitar a visualizaçao
print("\n" * 100)

# Cria a matriz A com valores inteiros (int)

matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])

print("Matriz A")
print(matriz_A)

# Eleva todos os elementos da matriz A ao cubo
matriz_B = power(matriz_A, 3)
print("\n")
print("Todos os elementos da matriz A elevados ao cubo")
print(matriz_B)