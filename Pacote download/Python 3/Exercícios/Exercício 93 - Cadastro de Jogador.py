jogador = dict()
gols = []

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
if jogador['partidas'] > 0:
    for g in range(1,jogador['partidas']+1):
        jogador['gols'] = int(input(f'Quantos gols na partida {g}? '))
        gols.append(jogador['gols'])
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-='*50)
print(jogador)
print('-='*50)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)

for i, v in enumerate(jogador['gols']):
    print(f'  -> Na partida {i+1}, fez {v} gols.')
