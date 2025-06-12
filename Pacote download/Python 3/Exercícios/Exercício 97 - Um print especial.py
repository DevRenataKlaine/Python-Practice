def escreva(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'  {texto}')
    print('-' * tam)

texto = str(input('Escreva um texto para deixá-lo centralizado: '))
escreva(texto)
