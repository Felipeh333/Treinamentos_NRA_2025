frase = input('Digite uma frase: ')

letra = 'a'

#mecanismo de detecção da última posição de a
invertida = ''
tamanho_frase = len(frase)

for i in range(tamanho_frase, 0, -1):
    invertida += frase[tamanho_frase - 1]
    tamanho_frase -= 1    

if frase.find(letra) != -1:
    print(f'A letra "{letra}" aparece {frase.count(letra)} vez(es), a primeira em {frase.find(letra) + 1} e a última em {len(frase) - invertida.find(letra) + 1}')
else:
    print(f'A frase não contém "{letra}"')
