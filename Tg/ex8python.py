soma_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):  
    print('----- {}ª PESSOA -----'.format(i))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().lower()

    soma_idade += idade

    if sexo == 'm':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print('\nA média de idade do grupo é {:.2f} anos.'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos.'.format(homem_mais_velho, idade_homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_menos_20))
