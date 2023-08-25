# n = bool(input('Digite algo: '))
# print(n)

n1 = input('É número? ')
print(n1.isnumeric()) # 2 - true, 3a false, w - false

n2 = input('É alfabético? ')
print(n2.isalpha()) # ww - true, 123 - false, 3a - false

n3 = input('É alfanumerico? ')
print(n3.isalnum()) # oi - true, 3a - true, espaço - false

n4 = input('É tudo MAIÚSCULO? ')
print(n4.isupper())

n5 = input('É tudo minúsculo? ')
print(n5.islower())

n6 = input('Pode ser impresso? ')
print(n6.isprintable())

n7 = input('É um espaço? ')
print(n7.isspace())





