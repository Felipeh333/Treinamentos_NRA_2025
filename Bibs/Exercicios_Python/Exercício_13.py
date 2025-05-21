# Desenvolvido por Beatriz Matias
# Exercício 13

frase = input("Digite uma frase: ").strip().upper()

print("\n Quantidade de letras 'A':", frase.count("A"))
print(" Primeira posição da letra 'A':", frase.find("A") + 1)  # Lembrar que somei 1 porque começa do 0
print(" Última posição da letra 'A':", frase.rfind("A") + 1)


