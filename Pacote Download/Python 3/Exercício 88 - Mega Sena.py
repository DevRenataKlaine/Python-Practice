from random import randint
lista = list()
jogos = list()

print('-'*30)
print('     JOGO DA MEGA SENA     ')
print('-'*30)

quant = int(input('Quantos jogos você quer que sejam sorteados? '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print()
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print()
print('-='*5, '< BOA SORTE! >', '-='*5)
