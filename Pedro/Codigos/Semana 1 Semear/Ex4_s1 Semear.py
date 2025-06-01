peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso/(altura*altura)

if imc < 18.5:
    print('Abaixo do peso')

elif imc >= 18.5 or imc < 25:
    print('Peso ideal')

elif imc >= 25 or imc < 30:
    print('Sobrepeso')

elif imc >= 30 or imc <= 40:
    print('Obesidade')

elif imc > 40:
    print('Obesidade Mórbida')