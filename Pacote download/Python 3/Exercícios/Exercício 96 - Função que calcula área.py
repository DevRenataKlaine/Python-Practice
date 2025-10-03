def area(larg, comp):
    resp = larg * comp
    print(f'A área de um terreno de {larg} x {comp} m é de {resp}m².')


#Programa Principal
print('CONTROLE DE TERRENOS')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
