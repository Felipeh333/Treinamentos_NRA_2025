reta1 = int(input('Comprimento da reta 1:'))
reta2 = int(input('Comprimento da reta 2:'))
reta3 = int(input('Comprimento da reta 3:'))

if reta1 > reta2:
    temp = reta2
    reta2 = reta1
    reta1 = temp

if reta2 > reta3:
    temp = reta2
    reta2 = reta3
    reta3 = temp

if reta1 > reta2:
    temp = reta2
    reta2 = reta1
    reta1 = temp    

if reta3 < reta1 + reta2:
    print("As retas podem fazer um triangulo")
    if reta1==reta2==reta3:
        print("O triaguo é equilatero")
    elif reta1!=reta2!=reta3:
        print("O triangulo é escaleno")
    else:
        print("O trinagulo é isoceles")    

else:
    print("As retas não podem fazer um triangulo")