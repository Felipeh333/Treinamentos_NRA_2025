# Desenvolvido por Beatriz Matias
# Exercício 7

mais_18 = 0
total_homem = 0
mulher_menos_20 = 0

while True:
    print("\nCadastro de pessoa:")
    idade = int(input("Idade: "))
    sexo = input("Sexo (m/f): ")

    if idade > 18:
        mais_18 += 1

    if sexo == "m":
        total_homem += 1

    if sexo == "f" and idade < 20:
        mulher_menos_20 += 1

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
    if continuar != "s":
        break

print("\n Pessoas com mais de 18 anos: ", mais_18)
print(" Homens cadastrados: ", total_homem)
print(" Mulheres com menos de 20 anos: ", mulher_menos_20)

