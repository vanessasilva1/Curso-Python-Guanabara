preco = float(input('Quanto custa esse produto? '))
desconto = float(input('Digite quantos % de desconto: '))

novoValor = preco - ((preco * desconto) / 100)

print('O valor do produto que custava R${:.2f}, com desconto de {}%, agora vale R${:.2f}'.format(preco, desconto, novoValor))
