n = int(input('Diga um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('O número que voçê escolheu é PRIMO')
else:
    print('O número que voçê escolheu NÃO É PRIMO')
