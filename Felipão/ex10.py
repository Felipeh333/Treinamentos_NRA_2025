num = 1

while num > 0:
    num = int(input('Digite um número: '))
    for i in range(1,11):
        print('{}x{} = {}'.format(num,i,num*i))