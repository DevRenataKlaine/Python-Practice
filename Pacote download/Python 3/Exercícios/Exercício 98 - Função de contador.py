from time import sleep


def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1  # Corrige passo zero
    if passo < 0:
        passo = -passo  # Garante passo positivo para lógica
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ', flush=True)
            sleep(0.5)
    else:
        for cont in range(inicio, fim - 1, -passo):
            print(cont, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
    print('-=' * 20)

# Contagem padrão
contador(1, 10, 1)

# Contagem regressiva
contador(10, 0, 2)

# Contagem personalizada
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim2 = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim2, pas)
