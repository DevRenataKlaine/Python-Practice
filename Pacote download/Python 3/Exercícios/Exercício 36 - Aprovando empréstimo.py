#Aprovando empréstimo
imovel = float(input('Para saber se eu empréstimo será aprovado, precisamos que você responda algumas perguntas. \nPrimeiramente, qual o valor do imóvel a ser adquirido? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos você pretende quitar o empréstimo? R$ '))
prestação = imovel / (anos * 12)
minimo = (salario*30) / 100      #até 30% do valor do salário
if prestação <= minimo:
    print('Para pagar um imóvel de R$ {:.2f} em {} anos, a prestação será de {:.2f}. \nSeu empréstimo pode ser CONCEDIDO!'.format(imovel, anos, prestação))
else:
    print('Para pagar um imóvel de R$ {:.2f} em {} anos, a prestação será de {:.2f}. \nInfelizmente seu empréstimo será NEGADO!.'.format(imovel, anos, prestação))