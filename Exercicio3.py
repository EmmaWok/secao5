print('Insira um número:')
num = float(input())

if num > 0:
    print(f'A raiz quadrada de {num} é {num ** 0.5:.2f}...')
else:
    print(f'{num} ao quadrado é -{num ** 2}')
