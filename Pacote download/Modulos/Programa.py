import uteis
from uteis import moeda, funções

print('EXERCÍCIO 106')
num = int(input('Digite um valor: '))
fat = funções.fatorial(num)
print(f'O fatorial de {num} é {uteis.fatorial(num)}.')
print(f'O dobro de {num} é {uteis.dobro(num)} e o triplo é {uteis.triplo(num)}')

print()
print('EXERCÍCIO 107')
p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

print()
print('EXERCÍCIO 108')
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 80, 35)
