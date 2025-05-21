#Autoria:Gustavo Leal Malafaia
#Data:17/05/2025
#Objetivo do progama:A partir da altura e peso de uma pessoa apresentar sua classificação quanto a seu IMC


peso = float(input('Qual o seu peso(em kg)? '))
altura = float(input('Qual a sua altura(em m)? '))

imc = peso/(altura**2)

print('Segundo o seu imc...')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com seu peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade')
elif imc >= 10:
    print('Você está com obesidade mórbida')
