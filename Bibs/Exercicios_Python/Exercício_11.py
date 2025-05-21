# Desenvolvido por Beatriz Matias
# Exercício 11

valor = int(input("Digite o valor a ser sacado: "))

cedula50 = valor // 50
valor = valor % 50

cedula20 = valor // 20
valor = valor % 20

cedula10 = valor // 10
valor = valor % 10

cedula1 = valor // 1

print("\n Número de cédulas que serão entregues:")
print(f"R$50: {cedula50}")
print(f"R$20: {cedula20}")
print(f"R$10: {cedula10}")
print(f"R$1:  {cedula1}")


