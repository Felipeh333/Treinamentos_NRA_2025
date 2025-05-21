# Autoria:Gustavo Leal Malafaia
# Data:17/05/2025
# Objetivo do programa:Realizar uma progressão aritmética

# Definição de variável inicial do código
n_repeticoes = 9


# Definição das constantes da PA
primeiro_termo = float(
    input('Insira o primeiro termo da Progressão Aritmética: '))
razao = float(input('Insira a razão da Progressão Aritmética: '))

# Primeiro laço de repetição de impressão dos 10 primeiros termos da PA
for i in range(n_repeticoes):
    ai = primeiro_termo + (i*razao)
    print(ai)

# Laço de repetição para a impressão de quantos termos da PA o usuário quiser
while True:
    n_termos = int(input(
        'Insira quantos termos a mais da progressão quer ver(se não quiser mais nenhum termo digite 0 para encerrar o programa): '))

    if n_termos == 0:
        break
    else:
        for i in range(n_termos):
            ai = primeiro_termo + ((i+n_repeticoes)*razao)
            print(ai)
    n_repeticoes += n_termos
