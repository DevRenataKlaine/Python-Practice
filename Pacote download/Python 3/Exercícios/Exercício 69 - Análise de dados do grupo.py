cont18 = contm = contf = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 20)
    if idade >= 18:
        cont18 += 1
    if sx in 'Mm':
        contm += 1
    if sx in 'Ff' and idade < 20:
            contf += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 20)
print(f'''Total de pessoas com mais de 18 anos: {cont18}
Ao todo temos {contm} homem(s) cadastrado(s)
e {contf} mulher(es) com menos de 20 anos.''')
