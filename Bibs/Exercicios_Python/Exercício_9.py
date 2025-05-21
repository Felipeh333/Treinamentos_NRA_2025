# Desenvolvido por Beatriz Matias
# Exercício 9

soma_num_pares = 0

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        soma_num_pares += num

print("\nA soma dos números pares é:", soma_num_pares)


