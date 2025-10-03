valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
    elif resp not in 'Ss':
        print('Resposta não identificada. Tente novamente!')
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
if 5 not in valores:
    print('O valor 5 não faz parte da lista!')
