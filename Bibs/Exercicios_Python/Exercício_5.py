# Desenvolvido por Beatriz Matias
# Exercício 5

a = float(input('\nQual o comprimento da reta a? '))
b = float(input('Qual o comprimento da reta b? '))
c = float(input('Qual o comprimento da reta c? '))

if a < b + c and b < a + c and c < a + b:
    print("\nOs segmentos formam um triângulo.\n")

    if a == b == c:
        print("Tipo: Triângulo Equilátero\n")
    elif a == b or a == c or b == c:
        print("Tipo: Triângulo Isósceles\n")
    else:
        print("Tipo: Triângulo Escaleno\n")

else:
    print("\nOs segmentos NÃO formam um triângulo.\n")