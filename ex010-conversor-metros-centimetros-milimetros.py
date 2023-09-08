metros = float(input('Digite um número em metros: '))

# transformar metros em KM ---- divide por 1000
# hectômetro HM - basta dividir por 100
# Decametro DAM = divide por 10
# Decimetro DM = multiplica por 10
# Centimetro CM = multiplica por 100
# Milímero MM = multiplica por 1000

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A medida de {:.1f} corresponde a'.format(metros))
print('{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))

