p = float(input())
h = float(input())

imc = p/(h*h)

if imc>40:
    print('Obesidade Mórbida')

elif imc>30 and imc<40:
    print('Obesidade')

elif imc>25 and imc<30:
    print('Sobrepeso')

elif imc>18.5 and imc<25:
    print('Peso ideal')

else:
    print('Abaixo do peso')