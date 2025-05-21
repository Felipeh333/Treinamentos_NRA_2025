# Desenvolvido por Beatriz Matias
# Exercício 6

primeiro = int(input('\nEscolha o primeiro termo: '))
razao = int(input('Escolha a razão da PA: '))

print('\nProgração Aritmética: ')
termo = primeiro
for i in range( 0, 10, 1):
    termo = primeiro + i * razao
    print(termo)

resposta = input('\n Quer mostrar mais um termo? (s para sim, n para não) ')

while resposta == "s":
    print('\n', termo)
    termo = termo + razao
    resposta = input('\n Quer mostrar mais um termo? (s para sim, n para não) ')