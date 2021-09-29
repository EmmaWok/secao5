print('Insira um número abaixo:')
num = float(input())

if num >= 1:
    print(f'{num} ao quadrado = {num ** 2}')
    print(f'A raíz quadrada de {num} é = {num ** 0.5}')

elif num < 1 :
    print('Número negativo')

else:
    print('Erro')
