from random import randint
pc = randint (0, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
n = int(input('Qual é seu palpite? '))
palpites = 0
while n != pc:
    if pc > n:
        palpites += 1
        n = int(input('Mais... Tente mais uma vez.'))
    elif pc < n:
        palpites += 1
        n = int(input('Menos... Tente mais uma vez.'))
if n == pc:
    palpites += 1
print('Você acertou com {} tentativa(s). Parabéns!'.format(palpites))
