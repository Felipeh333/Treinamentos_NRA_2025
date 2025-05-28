reta_1 = float(input('Digite o comprimento da reta 1'))

reta_2 = float(input('Digite o comprimento da reta 2'))

reta_3 = float(input('Digite o comprimento da reta 3'))

if (reta_1 > reta_2 + reta_3) (reta_2 + reta_3 > reta_1) or (reta_1 + reta_3 > reta_2):
    print('As retas não formam um triangulo')
else:
    if (reta_1 == reta_2) and (reta_2 == reta_3):
        print('As retas formam um trianulo equilatero')
    elif (reta_1 != reta_2) and (reta_2 != reta_3) and (reta_3 != reta_1):
        print('As retas formam um triangulo escaleno')
    else:
        print('As retas formam um triângulo isoceles')
