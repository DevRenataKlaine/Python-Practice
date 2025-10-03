print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = t1 + (10 -1) * razao
for c in range (t1, decimo + razao, razao):
    print(c, end=' - ')
print('ACABOU')