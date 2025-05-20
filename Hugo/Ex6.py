xii = float(input('Insira o termo inicial: '))
r2 = float(input('Insira a razão: '))
nii = 10
contador = 0
continuar = 1

while continuar == 1:
    for i in range(contador, nii):
        x1 = xii + i * r2
        print(x1)
        contador += 1
    else:
        continuar = int(input('Deseja mais termos? Se sim, digite 1. Caso não, digite outro número: '))
        if continuar == 1:
            y = int(input('Quantos termos a mais deseja?: '))
            while y < 1:
                print('Digite um número positivo diferente de zero:')
                y = int(input('Quantos termos a mais deseja?: '))
            nii += y  
        else:
            print('Programa encerrado.')