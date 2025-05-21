#Autoria:Gustavo Leal Malafaia
#Data:16/05/2025
#Objetivo do progama:A partir da altura e largura de uma parede poder dizer quantos litros de tinta serão necessários para pintá-la

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura*altura

tinta_necessaria = area/2

print(f'A quantidade de tinta necessária é {tinta_necessaria}L')