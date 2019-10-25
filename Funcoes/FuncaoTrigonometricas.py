# Importa funções trigonometricas (sin, cos e tan) da biblioteca math
# Importa também a constante pi e a função de conversão
# de graus para radianos (radians)
#
from math import sin, cos, tan, pi, radians

print("\n" * 100)

# Usa a função seno. Argumento em radianos
y = sin(pi / 2)

print("\n")
print("Resultado da função y = seno(pi/2)")
print(y)


# Usa a função cosseno. Argumento em radianos
y = cos(pi / 6)

print("\n")
print("Resultado da função y = cosseno(pi/6)")
print(y)


# Usa função tangente. Argumento em radianos
y = tan(pi / 4)
print("\n")
print("Resultado da função y = tangente(pi / 4)")
print(y)

# Usa função seno. Argumento em graus
angulo = radians(30)
y = sin(angulo)

print("\n")
print("Resultado da função y = seno(30)")
print("y = ", y)

# Usa função cosseno Argumento em graus
y = cos(radians(120))
print("\n")
print("Resultado da funçao y = cos(120)")
print("y = ", y)

# Usa função tangente. Argumento em graus
y = tan(radians(60))
print("\n")
print("Resultado da função y = tangente(60)")
print("y = ", y)
