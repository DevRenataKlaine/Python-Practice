print('-'*30)
print('LOJA RPK')
print('-'*30)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra foi R$ {total:.2f}.
Com {totmil} produto(s) custando mais de R$ 1000.00.
O produto mais barato foi {barato} que custa R$ {menor:.2f}.''')
