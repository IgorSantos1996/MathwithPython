# Importa bibilioteca numpy que permite trabalhar com matrizes
# Função matriz para definir matrizes
#
from numpy import matrix
# Limpa a área de console para facilitar à visualização do resultado
print("\n" * 100)

# Cria matriz A com valores inteiros (int)
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])
print("Matriz A")
print(matriz_A)

# Soma dos elmentos da matriz A por coluna
soma_colunas_A = matriz_A.sum(axis=0)
print("\n")
print("Soma dos slementos das colunas da matriz A")
print(soma_colunas_A)

# Soma dos elementos da matriz A por linha
soma_linhas_A = matriz_A.sum(axis=1)

print("\n")
print("Soma dos elementos das linhas da matriz A")
print(soma_linhas_A)

# Soma de todos os elementos da matriz A
soma_A = matriz_A.sum()
print("\n")
print("Soma de todos os elementos da matriz A")
print(soma_A)
