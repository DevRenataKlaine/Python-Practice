#base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif base == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')