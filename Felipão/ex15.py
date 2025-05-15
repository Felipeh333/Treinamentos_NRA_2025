def maior(a):
    maior = a[0]
    for i in range(1, len(a)):
        if a[i] > maior:
            maior = a[i]
    return maior