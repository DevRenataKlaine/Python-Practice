from random import randint
cont = 0

while True:
    n = int(input('Digite um valor: '))
    pc = randint(0, 10)
    resultado = n + pc
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {n} e o computador jogou {pc}. Total de {resultado} ', end='')
    if jogada == 'P':
        if resultado % 2 == 0:
            cont +=1
            print('DEU PAR!')
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')
            break
    elif jogada == 'I':
        if resultado % 2 == 1:
            cont += 1
            print('DEU íMPAR!')
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente!')
print('=-' *20)
print(f'GAME OVER! Você venceu {cont} vezes.')
