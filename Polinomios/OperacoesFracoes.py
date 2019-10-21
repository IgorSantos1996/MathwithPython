# Importa função Fraction (fração) da biblioteca fractionss
#
from fractions import Fraction

#Define frações
a = Fraction(1,4) # a = 1 /4
b = Fraction(2, 3) #b = 2/3
# Operacoes
soma = a + b
subtracao = a * b
multiplicacao = a * b
divisao = a / b

print("Resultado das operações com frações")
print(f"a = {a}")
print(f"a = {b}")
print(f"a + b = {soma}")
print(f"a - b = {subtracao}")
print(f"a * b = {multiplicacao}")
print(f"a / b = {divisao}")
