def leiaint (frase):
    while True:
        try:
            n = int(input(frase))
        except (TypeError):
            print('Isso não é um número inteiro')
            continue
        else:
            return n