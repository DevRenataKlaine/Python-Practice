#70kg mais leves / #100 kg mais pesadas
galera = list()
dado = list ()
cont = pesada = leve = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        pesada = leve = dado[1]
    else:
        if dado[1] > pesada:
            pesada = dado[1]
        if dado[1] < leve:
            leve = dado[1]
    galera.append(dado[:])
    dado.clear()
    cont += 1
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {pesada} kg. Peso de ', end='')
for p in galera:
    if p[1] == pesada:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leve} kg. Peso de ', end='')
for p in galera:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print()
