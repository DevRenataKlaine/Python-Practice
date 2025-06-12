linha1 = list()
linha2 = list()
linha3 = list()

linha1.append(list[int](input('Digite um valor para [0,0]: ')))
linha1.append(list[int](input('Digite um valor para [0,1]: ')))
linha1.append(list[int](input('Digite um valor para [0,2]: ')))
linha2.append(list[int](input('Digite um valor para [1,0]: ')))
linha2.append(list[int](input('Digite um valor para [1,1]: ')))
linha2.append(list[int](input('Digite um valor para [1,2]: ')))
linha3.append(list[int](input('Digite um valor para [2,0]: ')))
linha3.append(list[int](input('Digite um valor para [2,1]: ')))
linha3.append(list[int](input('Digite um valor para [2,2]: ')))

print('-='*30)
print(linha1)
print(linha2)
print(linha3)

# OUTRA POSSIBILIDADE

#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#   for l in range (0, 3):
#        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#print('-='*30)
#for l in range(0, 3):
#    for c in range(0, 3):
#        print(f'[{matriz[l][c]^5}]', end='')
#    print()
