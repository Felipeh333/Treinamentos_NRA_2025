frase = str(input('Digite uma frase: ')).lower().replace('' , '')

def palindromo_detect (frase):
    if frase == frase[::-1]:
        return True
    else:
        return False