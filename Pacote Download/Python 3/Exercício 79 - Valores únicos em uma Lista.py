valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).upper() [0]
    if resp in 'Nn':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
