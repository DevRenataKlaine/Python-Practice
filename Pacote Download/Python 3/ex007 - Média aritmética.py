nota1 = float (input ('Primeira nota do aluno: '))
nota2 = float (input ('Segunda nota do aluno: '))
media = (nota1 + nota2) /2
print ('A média entre {:.1f} e {:.1f} é igual a \033[1;31m{:.1f}\033[m'.format(nota1, nota2, media))
