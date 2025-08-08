'''
Escreva um programa em python que simule o calculo de notas de um aluno em diiferentes disciplinas. O programa deve modular e utilizar as estruturas de controle e funções.

1. Requisitos do sistema
 - Função calcular_media(notas)
    - Essa função deve receber uma LISTA de notas como parâmetro
    - Deve ter uma estrutura de repetição (for ou while) para percorrer a lista
    - Retornar a média das notas (com validações)
 - Função verificar_aprovacao(media, media_min)
    - Deve receber a média das notas e a médias minimas para aprovação
    - Deve usar condicionais para verificar o status do aluno
    - se a média for maior que a média minima, retornar a String "Aprovado"
    - se a média for maior ou igual a 5 e menor do que a média minima, retornar a String "Recuperação"
    - caso contrario, retornar a string "Reprovado"

 - Função Principal main()
    - Lista com as disciplinas
    - média minima para aprovação
    - estrutura de repetição para iterar sobre as disciplinas
    - para cada disciplina o usuario deve inserir 3 notas
    - chamar a função calcular_media(), para obter a média da disciplina
    - chamar a função verificar_aprovacao(), para obter o status
    - imprimir a media e o status para cada disciplina
'''


def calcular_media(notas):
    soma = 0

    # percorrer a lista de notas

    for nota in notas:
        soma = soma + nota  # acumular valor na variavel soma

    if len(notas) > 0:
        return soma / len(notas)
    else:
        return 0


def verificar_aprovacao(media, media_minima):
    if media >= media_minima:
        return "Aprovado"
    elif media >= 5.0 and media < media_minima:
        return "Recuperação"
    else:
        return "Reprovado"


def main():
    # lista com as disciplinas

    disciplinas = ["Python", "Java", "Banco de Dados"]
    media_aprovacao = 7.0

    print(f'\n*-- Sistema de Cálculo de notas --*\n')

    # percorre a lista de disciplinas
    for disciplina in disciplinas:
        print(f'Disciplina: {disciplina}')

        # lista com as notas
        notas = []

        for i in range(3):
            nota = float(input(f'Digite a nota {i + 1}: '))
            notas.append(nota)

        # Chamar as funções calcular_media e verificar_aprovacao
        media_final = calcular_media(notas)
        status = verificar_aprovacao(media_final, media_aprovacao)

        # Imprimir a media e o status
        print(f'Média em {disciplina}: {media_final:.2f}')
        print(f'Status: {status}')


main()