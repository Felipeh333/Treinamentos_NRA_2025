#Fiz o código considerando os espaços como caracteres, pois não foi dito nada sobre isso no enunciado:

frase = str(input('Insira aqui a frase: '))
if 'a' in frase.lower():  #Eu poderia aqui tomar também if frase.lower().find('a') != -1...
    print(f'A letra "A" aparece {frase.lower().count('a')} vezes.')
    print(f'O primeiro "A" está na posição {frase.lower().find("a")}.')
    print(f'O útlimo "A" está na posição {frase.lower().rfind("a")}.') #Achei esse método rfind() mais interessante nas videoaulas, 
    #mais simples que minha ideia inicial, que era usar o fatiamento [::-1] para inverter a string e usar o find normal
else:
    print('Não há a letra "A" na frase.')    