# Importa biblioteca numpy que permite trabalhar com matrizes
# Função matrix para definir matrizes
#
from numpy import matrix


# Cria matriz A com valores (int)
matriz_A = matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

# Cria matriz B com valores usando ponto flutuante (float)
matriz_B = matrix([
    [1.0, 2.2, 3.1],
    [4.6, 5.4, 6.7]
])
print('Matriz A')
print(matriz_A)
print("\n")
print("Matriz B")
print(matriz_B)

# Identifica dimensões da matriz A

dimensoes_matriz_A = matriz_A.shape
print("\n")
print("Dimensoes da matriz A: ")
print(dimensoes_matriz_A)

# Busca elemento da matriz B
# LEmbrar que para o Python, a primeira linha/coluna é zero
elemento_B_L0_C1 = matriz_B[0, 1]

print('\n')
print("Elemento da primeira linha e segunda coluna da matriz B")
print(elemento_B_L0_C1)
