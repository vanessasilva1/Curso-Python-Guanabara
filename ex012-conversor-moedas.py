real = float(input('Quanto dinheiro você tem na carteira? R$'))
cotacao = float(input('Qual o preço do dólar atual? US$'))
dolar = real / cotacao

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
