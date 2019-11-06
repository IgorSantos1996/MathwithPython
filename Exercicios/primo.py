# Algoritmo para informar se um dado numero, é primo.
primo = 1
numero = int(input("Informe o numero: "))
i = 2
for i in range(i, numero-1):
    if(numero % i == 0):
        primo = 0
        break
if(primo == 1):
    print("Numero primo")
else:
    print("Numero não é primo")
