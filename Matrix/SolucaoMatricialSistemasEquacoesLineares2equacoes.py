# Importa biblioteca numpy que permite trabahar com matrizes
# Funçlão matrix para definir matrizes
# Função linalg para fazer matriz inversa
#
from numpy import matrix, linalg

print("\n" * 100)
# Cria a matriz A
matriz_A = matrix([
    [2, -5],
    [3, 6]
])

# Cria a matriz B
matriz_B = matrix([
    [11],
    [3]
])
# Cria matriz inversa de A
matriz_inv_A = linalg.inv(matriz_A)

# Resolve o sistema de equações lineares
solucao = matriz_inv_A * matriz_B
print("O resultado do sistema de equações lineares")
print(solucao)