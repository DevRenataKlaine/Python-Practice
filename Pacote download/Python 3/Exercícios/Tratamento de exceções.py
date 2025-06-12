def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: digite um número inteiro inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
