divisor = 2
dividendo = 10

quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = +1
resto = x

print("%d / %d = %d (quociente) %d (resto)" % (dividendo, divisor, quociente, resto))