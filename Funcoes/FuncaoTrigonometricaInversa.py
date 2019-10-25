# Importa funções trigonometricas inversas
# (asin, cos e tan) da biblioteca math
# Importa também a função de conversão
# radianos para graus (degrees)
#
from math import asin, acos, atan, degrees

print("\n" * 100)

# Usa função arco seno. resultado em radianos e em graus
y = asin(0.9)
y_em_graus = degrees(y)
print("\n")
print("Resultado da função y = arcoseno(0.9) em graus")
print("y = ", y)

print("\n")
print("Resultado da função y = arcsen(0.9) em graus")
print("y = ", y_em_graus)

# Usa a função cosseno. Resultado em radianos e em graus
y = acos(0.5)
y_em_graus = degrees(y)
print("\n")
print("Resultado da função y = arccos(0.5) em graus")
print("y = ", y_em_graus)


# Usa função tangente. Resultado em radianos
y = atan(3)
print("\n")
print("Resultado da função y = arctan(3) em radianos")
print("y = ", y)
print("\n")
print("Resultado da função y = arctan(3) em graus")
print("y = ", degrees(y))
