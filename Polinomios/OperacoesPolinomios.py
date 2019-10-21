from numpy import polyadd, polysub
coeficientes_pol1 = [3, 2, -1]  # Define o polinomio 3x**2 + 2x - 1\n"
coeficientes_pol2 = [4, -1, 3]  # Define polinômio 4x**2 - x + 3\n"

# Adição de polinômios
resultado = polyadd(coeficientes_pol1, coeficientes_pol2)
print("Coeficientes do resultado da soma entre")
print(f"3x**2x - 2x -1 e 4x**2 - x + 3 é {resultado}")

# Subtração de polinômios
coeficientes_pol1 = [3, -2, -1]  # Define o polinomio 3x**2 - 2x + 1\n",
coeficientes_pol2 = [-2, 0, 4]  # Define polinômio -2x**2 + 4\n",
resultado = polysub(coeficientes_pol1, coeficientes_pol2)
print("Coeficientes do resultado da subtracao entre")
print(f"3x**2 - 2x + 1 e - 2x**2 + 4 é {resultado}")