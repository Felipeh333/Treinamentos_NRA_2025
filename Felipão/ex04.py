altura = float(input('Qual é sua altura em metros? \n'))
peso = float(input('Qual é seu peso em kg? \n'))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print ('Abaixo do Peso')
elif imc <= 25:
    print ('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')