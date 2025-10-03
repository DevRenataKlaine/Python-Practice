s = 0
cont = 0
for c in range (1, 7):
    n = int(input('Diga o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
        if n % 2 != 0:
            print('Não há números pares.')
print('Você informou {} números pares. O resultado da soma dos valores é {}.'.format(cont, s))

