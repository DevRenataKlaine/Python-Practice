from random import randint
from time import sleep
pc = randint(0,5)
print('=--' * 20)
print('Vou pensar número entre 0 e 5. Tente adivinhar...')
print('=--' * 20)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if player == 0:
    print('PARABÉNS, você acertou!')
else:
    print('VOCÊ ERROU, eu estava pensando no número {} e não no {}!'.format(pc, player))

