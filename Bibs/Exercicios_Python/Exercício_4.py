# Desenvolvido por Beatriz Matias
# Exercício 4

peso = float(input('\nQual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))

imc = peso / (altura**2)

if imc < 18.5:
    print('\nAbaixo do peso.\n')  

elif imc < 25:
    print('\nPeso ideal.\n')

elif imc < 30:
    print('\nSobrepeso.\n')

elif imc < 40:
    print('\nObesidade.\n')

else:
    print('\nObesidade Mórbida.\n')