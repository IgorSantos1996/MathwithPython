# Importa biblioteca numpy que permite trabalhar com matrizes
# Função matrix para definir matrizes
# Função zeros para criar matriz com valores 0
# Função ones para criar matriz com valores 1
# Função identity para criar matriz identidades
#
from numpy import zeros, ones, identity

# Limpa a área do console para facilitar a visualização do resultado
print('\n' * 100)

# Cria uma matriz com todos os elementos iguais de 0 ou 1
matriz_C = zeros((4, 3), dtype='int')  # Matriz com valores inteiros

print("\n")
print("Matriz 4x3 com todos os elementos iguais a 0 - Inteiros")
print(matriz_C)

matriz_D = ones((2, 3), dtype='float')  # Matriz com valores em ponto flutuante
print('\n')
print('Matriz 2 x 3 com todos os elementos iguais a 1.0 - Ponto Flutuante')
print(matriz_D)

# Cria matriz com todos os elementos iguais a um valor escolhido (neste caso 5.0)
matriz_E = 5 * (ones((4, 2), dtype='float'))
print('Matriz 4 x 3 com todos os elementos iguais a 5.0 - Ponto Flutuante')
print(matriz_E)

# Cria uma matriz identidade 3x3
matriz_F = identity(3)
print("\n")
print('MAtriz identidade 3 x 3')
print(matriz_F)
