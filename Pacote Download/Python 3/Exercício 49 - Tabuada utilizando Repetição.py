tabuada = int(input('Escolha uma tabuada: '))
for c in range (tabuada, tabuada*11, tabuada):
    print(c, end=' ')

#outra alternativa:
#for c in range(1, 11):
#   print('{} x {:2} = {}'.format(tabuada, c, tabuada*c))