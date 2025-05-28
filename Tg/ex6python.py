primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))

n = 10 

for i in range(n):
    ai = primeiro_termo + (i * r)
    print(ai)

while True:
    n_termos = int(input('Se deseja continuar a ver mais termos da progressão aritmética, digite o número, caso contrário, digite 0: '))
    
    if n_termos == 0:
        break
    else:
        for i in range(n, n + n_termos):
            ai = primeiro_termo + (i * r)
            print(ai)
        n += n_termos  

