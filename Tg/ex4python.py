
peso = float(input('Digite o seu peso em kg'))

altura = float(input('Digite sua altura em metros'))

imc = peso / (altura**2)

if (imc < 18.5):
    print ('Você está abaixo do peso')
    print ('seu imc é {}' .format(imc))
elif (18.5 <= imc < 25 ): 
    print ('Você está no peso ideal')
    print ('seu imc é {}' .format(imc))
elif (25 <= imc < 30):
    print ('Você está em sobrepeso')
    print ('seu imc é {}' .format(imc))
elif (30 <= imc < 40):
    print ('Você está obeso')
    print ('seu imc é {}' .format(imc))
else:
    print ('Você está em obesidade mórbida, procure um médico')
    print ('seu imc é {}' .format(imc))