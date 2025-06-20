from random import randint
from time import sleep
from operator import itemgetter

lista = []
ranking = list()

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()

print('>>> RANKING DE JOGADORES <<<')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
