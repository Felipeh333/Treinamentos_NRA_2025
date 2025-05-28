def maior(numeros_inteiros):
    if len(numeros_inteiros) == 0:
        return None
    else:
        maior_numero = numeros_inteiros[0]
        for num in numeros_inteiros:
            if num > maior_numero:
                maior_numero = num
        return maior_numero