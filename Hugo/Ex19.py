lista = []
lista_pares = []
lista_impares = []

n = int(input('Digite quantos números quer adicionar na lista: '))

for i in range(n):
    num = float(input(f'Digite o {i+1}° número: ')) 
    lista.append(num)

print(lista)

for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print()
print(f'Os números digitados foram {lista}')
print(f'Os números pares são: {lista_pares}')
print(f'Os números ímapres são: {lista_impares}')  
print()  