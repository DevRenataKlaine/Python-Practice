brasileirao2025 = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Red Bull Bragantino',
                   'Ceará', 'Bahia', 'Fluminense', 'Corinthians','Atlético-MG',
                   'Botafogo', 'São Paulo', 'Mirassol','Vasco da Gama', 'Fortaleza',
                   'Internacional', 'Vitória', 'Grêmio', 'Juventude', 'Santos', 'Sport')

print('-='*30)
print(f'Os cinco primeiros colocados são {brasileirao2025[0:5]}')
print('-='*30)
print(f'Os últimos 4 colocados são {brasileirao2025[-4:]}')
print('-='*30)
print('Lista em ordem alfabética: ', sorted(brasileirao2025))
print('-='*30)
print(f'O time Fortaleza está na {brasileirao2025.index('Fortaleza')+1}ª posição na classificação.')
