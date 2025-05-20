reta_1 = float(input('Qual o tamanho da reta 1 em centimetros? \n'))
reta_2 = float(input('Qual o tamanho da reta 2 em centimetros? \n'))
reta_3 = float(input('Qual o tamanho da reta 3 em centimetros? \n'))

if (reta_1 + reta_2 > reta_3) or (reta_2 + reta_3 > reta_1) or (reta_1 + reta_3 > reta_2):
    print('As retas não formam um triângulo')
else:
    if (reta_1 == reta_2) and (reta_2 == reta_3):
        print('As retas formam um triânulo equilátero!')
    elif (reta_1 != reta_2) and (reta_2 != reta_3) and (reta_3 != reta_1):
        print('As retas formam um triângulo escaleno')
    else:
        print('As reats formam um triângulos isóceles')