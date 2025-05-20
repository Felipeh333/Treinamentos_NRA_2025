import math

altura = float(input('Qual é a altura da parede? \n'))
largura = float(input('Qual é a largura da parede? \n'))
area = altura * largura

print('A parede possui {} metro(s) quadrado(s) e, para pintá-la, será(ão) necessária(as) {} lata(s) de tinta'.format(area, math.ceil(area/2)))