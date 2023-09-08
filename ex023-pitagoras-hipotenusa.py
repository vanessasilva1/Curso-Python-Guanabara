from math import sqrt, pow

catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Informe o cateto adjacente: '))

hipotenusa = sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))

print('A hipotenusa vale {:.2f}'.format(hipotenusa))

