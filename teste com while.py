salarios = [0,0,0,0]
soma = 0

i = 0
while i < len(salarios): #Tamanho da lista = 4
    salarios[i] = float(input("Salário R$: "))
    soma += salarios[i]
    i+=1

#calculando média salarial 
media = soma / len(salarios)

print(f"Média: {media:.2f}")

i=0
while i<len(salarios):
    if salarios[i] < media:
        print(f'Salário abaixo da média: {salarios[i]:.2f}')
    i+=1