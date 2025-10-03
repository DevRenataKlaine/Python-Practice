from random import randint

numeros = list()
pares = list()


def sorteia():
    for s in range(0, 5):
        numeros.append(randint(0, 10))
    print('Números sorteados: ', numeros, end='')
    print(' PRONTO!')


def somaPar():
    pares.clear()
    for valor in numeros:
        if valor % 2 == 0:
            pares.append(valor)
    soma = sum(pares)
    print(f'Somando os valores pares {pares}, temos {soma}.')


sorteia()
somaPar()
