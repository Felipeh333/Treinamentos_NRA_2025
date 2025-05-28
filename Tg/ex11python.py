valor = int(input("Digite o valor a ser sacado: R$"))

cedula = 50
total = valor

print("Notas entregues:")

while True:
    total_cedulas = total // cedula  
    total = total % cedula           

    if total_cedulas > 0:
        print("{} cédula(s) de R${}".format(total_cedulas, cedula))

   
    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    else:
        break  
