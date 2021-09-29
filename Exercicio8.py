print('Insira a nota do aluno:')
nota = float(input())
print('insira a segunda nota do aluno:')
nota2 = float(input())
media = (nota + nota2) / 2

if nota and nota2 <0.0 or nota and nota2 >10.0:
    print('Valor inválido.')
else:
    print(f'a Média é: {media}')
