F = M = 0
sx = str(input('Informe seu sexo: [F / M] ')).strip().upper()
while sx not in 'FfMm':
    sx = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
if sx in 'F':
    print('Você registrou seu sexo como FEMININO.')
elif sx in 'M':
    print('Você registrou seu sexo como MASCULINO.')
print('Obrigado pela sua resposta!')
