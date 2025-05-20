nome = input("Qual o seu nome? ")

lista = nome.split(' ')

print(f"\nMaiúsculas: {nome.upper()}\nMinúsculas: {nome.lower()}")
print(f"Quantas letras (sem espaços): {len(nome.replace(' ',''))}")
print(f"Número de caracteres do primeiro nome: {len(lista[0])}")
