homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0
sum_idades = 0

for _ in range(0, 4):
    nome = input('Qual o nome da pessoa que você quer cadastrar? ')
    idade = int(input('Qual a idade da pessoa que você quer cadastrar? \n'))
    sexo = input('Qual o sexo da pessoa que você quer cadastrar (H/M)? \n').strip().upper()

    sum_idades += idade

    if sexo == 'H' and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade

    if sexo == 'M' and idade < 20:
        mulheres_menos_20 += 1

media_idade = sum_idades / 4

print('\nA média de idade do grupo é de {:.2f} anos.'.format(media_idade))
if homem_mais_velho:
    print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(homem_mais_velho, idade_homem_mais_velho))
else:
    print('Não há homens no grupo.')
print('Há {} mulher(es) com menos de 20 anos.'.format(mulheres_menos_20))