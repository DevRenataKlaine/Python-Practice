pessoa = dict()
aposentadoria = 0

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = 2025 - nasc                                                      #opção sem datetime por questões técnicas
pessoa['CTPS'] = int(input('Nº da Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = ((pessoa['contratação'] + 35) - 2025) + pessoa['idade']
if pessoa['idade'] > 70:
    pessoa['aposentadoria'] = 'disponível'

print()
print('-'*30)
for k, v in pessoa.items() :
    print(f' - {k} tem o valor de {v}')
