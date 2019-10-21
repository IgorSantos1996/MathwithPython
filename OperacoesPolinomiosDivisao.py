from numpy import polydiv

coeficientes_pol1 = [4, 6, 3, 2]  # Define polinomio 1
coeficientes_pol2 = [2, 1, 2]  # Define polinomio 2
resultado1 = polydiv(coeficientes_pol1, 2)
resultado2 = polydiv(coeficientes_pol1, coeficientes_pol2)
print("Coeficientes do resultado da divisao de ")
print("4x**3 + 6x**2 + 3x + 2 por 2")
print(f'Coeficientes = {resultado1}')
print("Interpretando o resultado")
print("2x**3 + 3x**2 + 1.5x + 1 / resto 0")
print("\n")
print("Coeficientes do resultado da divisao de ")
print("4x**2 + 6x**2 + 3x + 2 por 2x**2 + x + 2")
print(f"Coeficientes = {resultado2}")
print("\n")
print("Interpretando o resultado: ")
print("Quociente 2x + 2 / Resto -3x -2")
