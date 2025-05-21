#Autoria:Gustavo Leal Malafaia
#Data:16/05/2025
#Objetivo do progama: A partir dos kilometros rodados e dias alugados calcular a tarifa a ser cobrada pelo aluguel de um carro

dias_alugados = float((input('Por quantos dias alugou o carro? ')))
km_percorridos = float((input('Andou quantos kilometros com o carro? ')))

preco_a_pagar = dias_alugados*60 + km_percorridos*0.15

print(f'O preço a pagar corresponde a R${preco_a_pagar}')