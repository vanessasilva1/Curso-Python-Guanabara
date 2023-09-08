salario = float(input('Qual o salário de um funcionário? '))
aumento = float(input('Qual o valor do aumento? '))

novoSalario = salario + ((salario * aumento) / 100)

print('Um funcionário que ganhava R${:.2f}, teve o aumento de R${:.2f}'.format(salario, novoSalario))