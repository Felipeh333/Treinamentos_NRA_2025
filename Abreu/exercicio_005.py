# Para existir um triangulo ABC, é preciso A < B + C para qualquer lado

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

# condição de existência
c1 = l2 + l3 > l1
c2 = l1 + l3 > l2
c3 = l1 + l2 > l3

resultado = (c1 and c2) and c3

if resultado == True:
    print('O triângulo de lados {}, {} e {} existe'.format(l1, l2, l3))

    # avalia, dado que é existente, qual o tipo de triângulo
    if l1 == l2 == l3:
        print('Ademais, ele é equilátero')
    elif l1 != l2 != l3:
        print('Ademais, ele é escaleno')
    else:
        print('Ademais, ele é isósceles')

else:
    print('O triângulo de lados {}, {} e {} não existe'.format(l1, l2, l3))
