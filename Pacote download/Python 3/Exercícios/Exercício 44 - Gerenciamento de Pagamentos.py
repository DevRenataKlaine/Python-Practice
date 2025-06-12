print('FINALIZE SEU PAGAMENTO')
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque (10% de desconto)
[ 2 ] à vista cartão (5% de desconto)
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
op = int(input('Escolha uma opção: '))
if op == 1:
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, preco - (preco*10/100)))
elif op == 2:
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, preco - (preco*5/100)))
elif op == 3:
    print('Sua compra será parcelada em 2x de R$ {} SEM JUROS.'.format(preco/2))
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif op == 4:
    parcelas = int(input('Em quantas parcelas você deseja realizar seu pagamento? '))
    juros = preco*20/100
    parcelasjuros = (juros + preco) / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, parcelasjuros))
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, preco + juros))
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')