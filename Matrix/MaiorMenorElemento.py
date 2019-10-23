# Importa biblioteca numpy que permite trabalhar com matrizes
# Função matrix para definir matrizes
# Função tranpose para fazer matriz transposta
#
from numpy import matrix

print("\n" * 100)

# Cria matriz A com valores inteiros (int)
matriz_A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

print('Matriz A')
print(matriz_A)

# Identificar maior e menor valores de matriz A
maior_valor_A = matriz_A.max()
menor_valor_A = matriz_A.min()
print("\n")

print("Maior valor na matriz A")
print(maior_valor_A)

print("\n")
print("Menor valor na matriz A")
print(menor_valor_A)

