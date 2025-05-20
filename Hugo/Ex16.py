def leiaInt(valor):
    while True:
        entrada = input(valor).strip()
        if entrada == '':
            print('Digite um número inteiro válido.')
            continue  #Descobri que o continue é uma opção melhor que criar outro while 

        if entrada[0] == '-':
            parte_numerica = entrada[1:]
            if parte_numerica == '':
                print('Digite um número inteiro válido.')
                continue
        else:
            parte_numerica = entrada

        _verifica_numero = True
        for caractere in parte_numerica:
            if caractere not in '0123456789':
                _verifica_numero = False
                break

        if _verifica_numero == True:
            return int(entrada)
        else:
            print('Digite um número inteiro válido.')


numero = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {numero}')
