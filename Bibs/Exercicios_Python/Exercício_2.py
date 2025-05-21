# Desenvolvido por Beatriz Matias
# Exercício 2

largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))

area = largura * altura
litro = area/2

print('Para pintar uma parede de {} metros quadrados é necessário {} litros de tinta.' .format(area, litro))