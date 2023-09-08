from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))

radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('O ângulo de {:.1f} tem o SENO de {:.2f}\nO COSSENO de {:.2f}\nE o TANGENTE é {:.2f}'
      .format(angulo, seno, cosseno, tangente))

