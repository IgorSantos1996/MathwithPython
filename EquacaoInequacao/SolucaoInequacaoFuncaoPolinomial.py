# Importa duncao Poly, para definir o polinômio
# Indica que x é a varaivel independente de sympy.abc
# Importa função solve_poly_inequality de sympy.solvers.inequalities
# para resolver inequações polinomiais
#
from sympy import Poly
from sympy.abc import x
from sympy.solvers.inequalities import solve_poly_inequality

# Limpa a area de console para facilitar a visualização dos resultados
print("\n" * 100)
resultado = solve_poly_inequality(Poly(3 * x - 7, x), '!=')
print("Solução da inequação 3* x - 7 != 0")
print(resultado)
print("Interpretando resultado")

print("Solução x < 7/3 ou x > 7/3. Que é o mesmo que x != 7/3.")
print("\n")
