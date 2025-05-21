# Autoria:Gustavo Leal Malafaia
# Data:17/05/2025
# Objetivo do programa:Dizer se um triângulo pode ser construído a partir de 3 segmentos de reta e classificar o triangulo se puder ser construido

# Observações:
# Em um triangulo a soma dos comprimento de qualquer dois lados deve resultar em um valor maior do que o comprimento do lado restante
# Onde se lê reta se quer dizer segmentos de reta

reta_A = float(input('Insira o comprimento da reta A:'))
reta_B = float(input('Insira o comprimento da reta B:'))
reta_C = float(input('Insira o comprimento da reta C:'))

# Variável booleana que indica se é possivel construir um triângulo com as retas apresentadas(seguindo a relação a+b > c para todas a as arestas)
triangulo_possivel = ((reta_A+reta_B) > reta_C) and ((reta_A+reta_C)> reta_B) and ((reta_B+reta_C) > reta_A)

# Divisão de casos em ser possivel ou não construir o triângulo e se for possivel se classifica o tipo de triângulo que pode ser feito
if not triangulo_possivel:
    print('Não é possivel construir um triângulo com estas retas')

elif triangulo_possivel:
    if reta_A == reta_B == reta_C:
        print('É possivel construir um triangulo equilátero com estas retas')
    elif reta_A == reta_B or reta_B == reta_C or reta_A == reta_C:
        print('É possivel construir um triangulo isósceles com estas retas')
    elif reta_A != reta_B != reta_C:
        print('É possivel construir um triangulo escaleno com estas retas')
