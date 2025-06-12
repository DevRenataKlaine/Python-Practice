cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
primeiro = cidade.split()[0]
encontrar = 'santo' in primeiro
print(encontrar)
