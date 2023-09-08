from math import hypot
catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Informe o cateto adjacente: '))

hipotenusa = hypot(catOposto, catAdjacente)
print('A hipotenusa vale {:.2f}'.format(hipotenusa))
