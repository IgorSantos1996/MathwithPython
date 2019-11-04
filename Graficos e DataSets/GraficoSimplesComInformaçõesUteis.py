import matplotlib.pyplot as p

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

p.title('Faturamento no primeiro semestre de 2019')
p.xlabel('Meses')
p.ylabel('Faturamento em R$')

p.plot(meses, valores)
p.ylim(100000, 120000)
p.show()
