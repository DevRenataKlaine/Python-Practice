L = float (input('Largura da parede: '))
A = float (input('Altura da parede: '))
area = L * A
tinta = area /2
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.3f}m².'.format(L, A, area))
print('Para pintar essa parede, você precisará de {:.4f} litros de tinta.'.format(tinta))
