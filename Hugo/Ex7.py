cadastro = []
p_18 = 0
h = 0
m_20 = 0
i = 1

while True:
    print('\n')
    print(f'Pessoa {i}:')
    idade = int(input('Insira a idade: '))
    while idade < 0:
        idade = int(input('Insira um valor válido para a idade: '))

    sexo = str(input('Sexo (M/F): '))

    pessoa = (idade, sexo)
    cadastro.append(pessoa)
    i += 1

    decisao = int(input('Digite 1 se deseja adicionar mais uma pessoa. Caso contrário, digite qualquer outro número: '))
    print('\n')
    if decisao != 1:
        break

for idade, sexo in cadastro:
    if idade > 18:
        p_18 += 1

    if sexo == 'M' or sexo == 'm':
        h += 1

    if (sexo == 'F' or sexo == 'f') and idade < 20:
        m_20 += 1

print(f'O número de pessoas com mais de 18 anos é {p_18};')
print(f'O número de homens é {h};')
print(f'O número de mulheres com menos de 20 anos é {m_20}.')                