a = float(input('Insira o valor do lado "a": '))
b = float(input('Insira o valor do lado "b": '))
c = float(input('Insira o valor do lado "c": '))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print('O triângulo existe e é equilátero!')
    elif a == b or b == c or a == c:
        print('O triângulo existe e é isóceles!')
    else:
        print('O triângulo existe e é escaleno!')    

else:
    print('O triângulo não existe!')