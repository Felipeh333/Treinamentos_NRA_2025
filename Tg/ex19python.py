numeros = []
pares = []
impares = []





print('Digite quantos números quiser, digite -1 quando quiser parar')
while True:
    n = int(input('Número:'))
    if n ==-1:
        break
    numeros.append(n) 

    if n % 2 == 0:
        pares.append(n)
    else: 
        impares.append(n)

print ('Todos:', numeros)
print ('Impares:', impares)
print ('Pares:', pares)
