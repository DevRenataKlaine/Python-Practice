peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura **2)
print('O IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Essa pessoa está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Essa pessoa está no peso ideal.')
elif 25 <= imc < 30:
    print('Essa pessoa está com sobrepeso.')
elif 30 <= imc < 40:
    print('Essa pessoa está com obesidade.')
else:
    print('AVISO! Essa pessoa está com obesidade mórbida.')