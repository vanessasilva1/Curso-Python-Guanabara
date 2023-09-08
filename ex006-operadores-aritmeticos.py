nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
subtracao = n1 - n2
multi = n1 * n2
divisao = n1 / n2
divInteira = n1 // n2
potencia = n1 ** n2
resto = n1 % n2

print('A soma vale {}, a subtracao vale {}, o produto vale {}, e a divisão vale {:.3f}'.format(soma, subtracao, multi, divisao), end=' >>> ')
print(' Divisão inteira  = {} \n Potência = {} \n Resto da divisão = {}'.format(divInteira, potencia, resto))
