n = int(input("Digite um valor a ser sacado: "))

notas_50 = n // 50
notas_20 = (n - notas_50 * 50)  // 20
notas_10 = (n - notas_50 * 50 - notas_20 * 20) // 20
notas_01 = n - notas_50 * 50 - notas_20 * 20 - notas_10 * 10

print(f"O número de cédulas é:\n{notas_50} de R$50,00\n{notas_20} de R$20,00\n{notas_10} de R$10,00\n{notas_01} de R$1,00")
