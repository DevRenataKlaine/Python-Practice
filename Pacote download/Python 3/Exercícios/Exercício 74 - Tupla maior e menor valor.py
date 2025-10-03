from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteado foram: ',end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO menor valor gerado foi {min(numeros)} e o maior foi {max(numeros)}.')
