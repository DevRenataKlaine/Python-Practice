print('=-' *15)
print('ANALISADOR DE TRIÂNGULOS')
print('=-' *15)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if (seg1 + seg2 > seg3) and (seg2 + seg3 > seg1) and (seg1 + seg3 > seg2):
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
