idade_18 = 0
sexo_homem = 0
sexo_mulher_20 = 0

while True: 
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (Masculino/Feminino): ').strip().lower()

    if idade > 18:
        idade_18 += 1
    
    if sexo == "masculino":
        sexo_homem += 1
    
    if sexo == "feminino" and idade < 20:
        sexo_mulher_20 += 1

    prosseguir = input("Deseja prosseguir com o cadastro de outra pessoa? (s/n): ").strip().lower()
    if prosseguir != "s":
        break

print('Pessoas com mais de 18 anos:', idade_18)
print('Homens cadastrados:', sexo_homem)
print('Mulheres com menos de 20 anos:', sexo_mulher_20)

