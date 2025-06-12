d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(d))
preço = d*0.5 if d <= 200 else d*0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
