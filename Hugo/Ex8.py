#Esse códugo em específico eu vou comentar todos os meus passos, pois ele usou praticamente tudo que estudei nesse PDF 
# e eu achei bem bacana!


#Criando a lista que vai guardar os cadastros e criando os cadastros pra 4 pessoas:
lista = []

for i in range(1,5):
    print(f'Pessoa {i}')
    nome = (input('Insira seu nome: '))
    idade = int(input('Insira sua idade: '))
    while True:
        sexo = (input('Informe seu sexo (M/F): '))
        if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':  #condicão que garante apenas respostas coerentes
            break           
        print('Erro, digite M para masculino e F para feminino: ')   
            
    print('\n')

    pessoa = (nome,idade,sexo)
    lista.append(pessoa)

#Média das idades das pessoas:
soma = 0
for pessoa in lista:
    soma += pessoa[1]    #Posição na tupla onde estão armazenada as idades são acessadas e somadas na iteração

media = soma/len(lista)

#Aqui eu criei uma verificação da existência de homens e e mulheres usando variáveis booleanas, pois quando eu rodei o código e inseri
#apenas mulheres, o o print ficava estranho, pois era algo como print(f'A média é {média}, o homem mais velho é {x} e há 
#{y} mulheres com menos de 20 anos'), e isso ficava estranho pois nestes campos de variáveis apareciam as variáveis
# "temporárias", que criei no for para buscar a maior idade ou idades menores que 20:

h = False  #começa assumindo que não há homens
for pessoa in lista:
    if pessoa[2] == 'M' or pessoa[2] == 'm':
        h = True
    
m = False  #começa assumindo que não há mulheres
for pessoa in lista:
    if pessoa[2] =='F' or pessoa[2] == 'f':
        m = True

#Abaixo está o for que verifica as tuplas e as listas, e procura pelos itens pedidos. Abaixo estão as 3 primeiras variáveis "temporárias"
#que criei para o for, com o objetivo de servirem como comparadores ou contadores:

nome_maior = ''     
maior_idade = -1
contador_mulher = 0
for pessoa in lista:
    if pessoa[2] == 'M' or pessoa[2] == 'm':
        if pessoa[1] > maior_idade:
            maior_idade = pessoa[1]
            nome_maior = pessoa[0]
    if pessoa[2] == 'F' or pessoa[2] == 'f':
        if pessoa[1] < 20:
            contador_mulher += 1

#Respostas de acordo com a  "permutação" dos casos em que coexistem ou existem separadamente:

if h == True and m == True:
    print(
        f'A média das idades é {media} anos, o homem mais velho é o {nome_maior}, com {maior_idade} anos, e há {contador_mulher} mulher(es)'
        'com menos de 20 anos.')
elif h == True and m == False:
    print(f'A média das idades é {media} anos, o homem mais velho é o {nome_maior}, com {maior_idade} anos, e não há mulheres.')
elif (h == False and m == True):
    print(f'A média das idades é {media} anos, não há homens e há {contador_mulher} mulher(es) com menos de 20 anos.')