maiores_idade = 0
homens = 0
mulheres_menor_20 = 0

while True:
    idade = int(input("Quantos anos? "))
    sexo = input("Qual o sexo (M/F)? ")
    
    if idade > 18:
        maiores_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    
    continuar = input("Deseja continuar (S/N)? ")
    if continuar == 'N':
        print(f"Maiores de 18: {maiores_idade}")
        print(f"Homens: {homens}")
        print(f"Mulheres menores que 20: {mulheres_menor_20}")
        break
