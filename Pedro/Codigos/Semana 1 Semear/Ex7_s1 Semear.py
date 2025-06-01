idade = []
sexo = []

control = 1
m = 0
f = 0
i = 0

while(control == 1):
    sexo.append(input("Sexo da pessoa:"))
    idade.append(int(input("Idade da pessoa:")))

    control = int(input("Se voce quer adicionar mais usuarios digite 1, se ja terminou digite 0 :"))

for n in idade:
    if n > 18:
        i += 1

for n in sexo:
    if n == "masculino":
        m += 1

for n in range(0,len(idade),1):

    if idade[n] < 20 and sexo[n] == "feminino":

        f += 1; 

print("Numero de pessoas com mais de 18 anos: {}".format(i))
print("Numero de pessoas do sexo masculino: {}".format(m))
print("Nunero de pessoas do sexo feminino com menso de 20 anos: {}".format(f))