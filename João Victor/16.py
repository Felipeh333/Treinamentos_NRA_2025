def leiaInt():
        
        try:
            valor = int(input())
            return valor
        
        except ValueError:
            print('erro')

n = leiaInt()

print(type(n))