digitar = input('Digite algo: ') #input sempre é string

print('O tipo primitivo desse valor é {}'.format(type(digitar)))
print('Só tem espaços? {}'.format(digitar.isspace()))
print('É um número? {}'.format(digitar.isnumeric()))
print('É alfabético? {}'.format(digitar.isalpha()))
print('É alfanúmerico? {}'.format(digitar.isalnum()))
print('Está em maiúsculas? {}'.format(digitar.isupper()))
print('Está em minúsculas? {}'.format(digitar.islower()))
print('Está capitalizada? Se tem maiúsculas e minúsculas juntas? {}'.format(digitar.istitle()))

s1 = set(range(10, 7, -1))
print(s1)