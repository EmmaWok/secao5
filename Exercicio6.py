print('Insira um número abaixo:')
num = int(input())
print('Insira outro número abaixo:')
num1 = int(input())

if num > num1:
    print(f'{num} é maior que {num1} e a diferença entre eles é de {num - num1}')
else:
    print(f'{num1} é maior que {num} e a diferença entre eles é de {num1 - num}')
