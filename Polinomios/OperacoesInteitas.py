# Importa funções ceil e floor da biblioteca math
#
from math import ceil, floor
# Limpa a área de console para facilitar a visualização do resultado
print('\n' * 100)
# Define valores
a = 3.456
b = 7.890

# Operacoes inteiras
piso_a = floor(a)
teto_a = ceil(a)

piso_b = floor(b)
teto_b = ceil(b)

print("Resultado das operações inteiras: ")
print(f"Piso de a = {piso_a}")
print(f"Teto de a = {teto_a}")
print("\n")
print(f"Piso de b = {piso_b}")
print(f"Teto de b = {teto_b}")
