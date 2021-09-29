print('Insira abaixo um número inteiro:')
num = int(input())

print('Insira abaixo outro número inteiro:')
num1 = int(input())

if num > num1:
    print(f'{num} é maior que {num1}')
elif num == num1:
    print('Números iguais')
else:
    print(f'{num1} é maior que {num}')
