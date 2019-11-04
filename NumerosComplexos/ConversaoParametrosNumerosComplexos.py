# Importa Funções de tratamento de numeros complexos da biblioteca cmath
# Função polar para conversão de forma retangular para a polar
# Função pahse para identificar a fase de um numero complexo
#
from cmath import polar, phase

# Importa a função de conversão de radianos para graus
from math import degrees

# Importa a função conj da biblioteca numpy para encontar o conjugado do numero complexo
from numpy import conj

print("\n" * 100)

# Define um numero complexo na forma retangular
z1 = -3 + 4j

print("Numero complexo -3 + 4j")
print("\n Forma retangular z1 = ", z1)
print("\n Conjugado de z1 = ", conj(z1))
print("\n Parte real de z1 = ", z1.real)
print("\n Parte imaginaria de z1 = ", z1.imag)
print("\n (Forma Polar) z1 = ", polar(z1))  # Conversão de z1 para polar
print("\n Modulo de z1 = ", abs(z1))
print("\n Argumento (radianos) de z1 = ", phase(z1))
print("\n Argumento (graus) de z1 = ", degrees(phase(z1)))
