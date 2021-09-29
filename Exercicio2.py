print('Insira um numero positivo:')
num = float(input())

if num > 0:
    print(f'A raiz quadrada de {num} é {num ** 0.5}')
else:
    print('Número inválido, tente novamente:')
    num = float(input())
    print(f'A raiz quadrada de {num} é {num ** 0.5}')
