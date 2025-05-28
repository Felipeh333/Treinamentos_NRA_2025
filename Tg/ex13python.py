
frase = input("Digite uma frase: ").strip().lower()


quantidade_a = frase.count('a')

primeira_posicao = frase.find('a') + 1
ultima_posicao = frase.rfind('a') + 1


print("A letra 'A' aparece {} vezes.".format(quantidade_a))
print("A primeira letra 'A' aparece na posição {}.".format(primeira_posicao))
print("A última letra 'A' aparece na posição {}.".format(ultima_posicao))
