x = 0

def voto(ano):
    idade = 2025 - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O VOTO É OPCIONAL'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
