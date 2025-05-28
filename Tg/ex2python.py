largura = float(input('Qual a largura da parede em metros?'))
altura = float(input('Qual a altura da parede em metros?'))

área = altura * largura 
litro = área/2 

print('A quantidade de tinta necessária para pintar a área de {} é {}'.format(área, litro))
