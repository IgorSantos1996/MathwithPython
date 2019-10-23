# Importa biblioteca numpy que permite trabalhar com matrizes
# Função matrix para definir matrizes
#

from numpy import matrix

# Limpa a área de console para facilitar a visualização do resultado
print("\n" * 100)

# Cria matriz A com valores inteiros (int)
matrix_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])
print("Matriz A")
print(matrix_A)

# Identificar maior e menor valores da matriz A
maior_valor_A = matrix_A.max(axis=0)
menor_valor_A = matrix_A.min(axis=1)

print("\n")
print("Maior valor de cada coluna da matriz A")
print(maior_valor_A)

print("\n")
print("Menor valor de cada linda da matriz A")
print(menor_valor_A)
