from datatime import date
atual = date.today().year
nascimento = int(input('Qual a seu ano de nascimento?'))
age = atual - nascimento
print('O atleta tem {} anos.'.format(age))
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JUNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')