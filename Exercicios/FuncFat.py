# Fatorial de 3: 3 * 2 * 1 = 6
# fatorial de 4: 4 * 3 * 2 * 1 = 24
# Fatorial de 5 = 5 * 4 * 3 * 2 * 1 = 120

def fatorial(numero):
    f = 1
    while numero > 1:
        f = numero * f
        print("(f=%d, numero=%d) " % (f, numero))
        numero -= 1
    return f


fatorial(10)
