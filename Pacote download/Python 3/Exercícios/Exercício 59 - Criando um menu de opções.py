v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != '5':
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('=' * 10)
    opcao = str(input('>>>> Qual é a sua opção?'))
    if opcao == '1':
        print('A soma entre {} + {} é {}.'.format(v1, v2, v1+v2))
    elif opcao == '2':
        print('A multiplicação entre {} x {} é {}.'.format(v1, v2, v1*v2))
    elif opcao == '3':
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior número entre {} e {} é {}.'.format(v1, v2, maior)) #não sei
    elif opcao == '4':
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao not in '1,2,3,4,5':
        print('Opção inválida. Tente novamente!')
print('='*10)
print('Fim do programa. Volte sempre!')
