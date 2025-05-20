razao = int(input('Razão da PA: '))
print('Os primeiros 10 termos da PA de razão {}: '.format(razao))

ultimo_valor = 0
for i in range(0, 10, 1):
    ultimo_valor += razao
    print(ultimo_valor)

else:
    resp = input('Responda "sim" ou "não" \nDeseja ver os próximos 5 termos? ')
    
    if resp == 'sim':
        for n in range(0, 5, 1):
            ultimo_valor += razao
            print(ultimo_valor)
        else:
            print('PA encerrada')
    else:
        print('PA encerrada')
