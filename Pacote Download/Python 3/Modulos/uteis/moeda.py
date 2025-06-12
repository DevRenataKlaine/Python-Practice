def aumentar(a, b):
    porc = (a * b) / 100
    resultado = a + porc
    return resultado


def diminuir(a, b):
    porc = (a * b) / 100
    res = a - porc
    return res


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def resumo(n, aum, dim):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:     R$ {n}')
    print(f'Dobro do preço:      R$ {dobro(n)}')
    print(f'Metade do preço:     R$ {metade(n)}')
    print(f'{aum}% de aumento:      R$ {aumentar(n, aum)}')
    print(f'{dim}% de redução:      R$ {diminuir(n, dim)}')
    print('-' * 30)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO: digite um número inteiro inválido!\033[m')
        if ok:
            break
    return valor


