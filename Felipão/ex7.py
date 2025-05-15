flag = True

maiores = 0
homens = 0
mulheres_menores_de_20 = 0

while flag:
    print('Central de Cadstros \n')
    idade = int(input('Qual a idade da pessoa que você quer cadastrar? \n'))
    sexo = input('Qual o sexo da pessoa que você quer cadastrar (H/M)? \n')

    if idade >= 18:
        maiores += 1
    if sexo == 'H':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulheres_menores_de_20 += 1
    
    flag = int(input('Deseja cadastrar mais alguém? Digite 1 para sim e 0 para não.')) == 1

print('Foram cadastrados: \n {} Maiores de idade \n {} Homem(s) \n {} Mulheres com menos de 20 anos'.format(maiores,homens,mulheres_menores_de_20))