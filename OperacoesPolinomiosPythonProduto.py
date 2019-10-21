from numpy import polymul, polydiv
coeficientes_pol1 = [2, 4, 0.5]  # Define o polinomio 1
coeficientes_pol2 = [3, 2, 0]  # Define o polinômio o 2

# Adição de polinômios
resultado1 = polymul(coeficientes_pol1, 2)
resultado2 = polymul(coeficientes_pol1, coeficientes_pol2)
print("Coeficientes do resultado do produto entre")
print(f" 2x**2 + 4x + 1/2 por 2 ")
print(f"Coeficientes = {resultado1}")
print(f"2x**2 + 4x + 1/2 e 3x**2 + 2x")
print(f"Coeficientes = {resultado2}")
