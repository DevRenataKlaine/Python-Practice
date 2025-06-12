valor = []
maior = menor = 0

for cont in range (0, 5):
    valor.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        if valor[cont] < menor:
            menor = valor[cont]

print('=-'*30)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} na(s) posição/posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi {menor} na(s) posição/posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}... ', end='')
print()
