salarios = []
soma = 0

for i in range(4):
    salario = float(input('Salário R$: '))
    salarios.append(salario)
    soma += salario

media = soma / len(salarios)

for salario in salarios:
    if salario < media:
        print(f'Salário abaixo da média: {salario:.2f}')