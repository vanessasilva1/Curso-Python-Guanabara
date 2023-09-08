from random import choice

primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))

lista = [primeiro, segundo, terceiro, quarto]

escolhido = choice(lista)

print('O aluno(a) escolhido(a) foi: {}'.format(escolhido))