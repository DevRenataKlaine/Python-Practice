v = int(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você escedeu o limite permitido que é 80km/h')
    multa = (v-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')