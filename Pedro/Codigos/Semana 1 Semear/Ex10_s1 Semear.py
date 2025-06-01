tabuada =[]

while True:
    
    num = int(input())

    if num < 0: 
        
        print("Número inválido")
        break

    print(f"Tabuada {num}:")

    for i in range (1,11):
        print(f"{num} x {i} = {num * i}")