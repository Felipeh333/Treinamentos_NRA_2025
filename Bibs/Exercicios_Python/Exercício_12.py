# Desenvolvido por Beatriz Matias
# Exercício 12

nome = input("Digite seu nome completo: ").strip()

print("\n Nome em maiúsculas:", nome.upper())
print(" Nome em minúsculas:", nome.lower())
print(" Total de letras (sem espaços):", len(nome.replace(" ", "")))
print(" Quantas letras no primeiro nome:", len(nome.split()[0]))

