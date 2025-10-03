dados = dict()
pessoas = list()
soma = 0

while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
    elif resp not in 'Ss':
        print('Resposta não identificada. Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'Nn':
            break
media = soma / len(pessoas)
print()
print('=-'*30)
print()
print(f'A) Ao todo, temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:3.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média de idade: ')
for p in pessoas:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'        {k} = {v}; ', end='')
print()
print()
print('<<<ENCERRADO>>>')
